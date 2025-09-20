#!/usr/bin/env python3
"""
System Health Monitoring Dashboard for Data Center Technician
Designed for Amazon Data Center Technician role portfolio
"""

import psutil
import platform
import time
import os
from datetime import datetime
import socket
import logging
from typing import Dict, List, Tuple

# Set up logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SystemHealthDashboard:
    def __init__(self, refresh_interval=5):
        self.refresh_interval = refresh_interval
        self.thresholds = {
            'cpu_warning': 80,
            'cpu_critical': 90,
            'memory_warning': 75,
            'memory_critical': 85,
            'disk_warning': 80,
            'disk_critical': 90,
            'temp_warning': 70,
            'temp_critical': 80
        }
    
    def get_system_info(self) -> Dict:
        """Get basic system information"""
        try:
            boot_time = datetime.fromtimestamp(psutil.boot_time())
            return {
                'hostname': socket.gethostname(),
                'os': f"{platform.system()} {platform.release()}",
                'processor': platform.processor(),
                'boot_time': boot_time.strftime("%Y-%m-%d %H:%M:%S"),
                'uptime': str(datetime.now() - boot_time).split('.')[0]
            }
        except Exception as e:
            logging.error(f"Error getting system info: {e}")
            return {}
    
    def get_cpu_usage(self) -> Tuple[float, str]:
        """Get CPU usage with status indicator"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            status = "NORMAL"
            if cpu_percent > self.thresholds['cpu_critical']:
                status = "CRITICAL"
            elif cpu_percent > self.thresholds['cpu_warning']:
                status = "WARNING"
            return cpu_percent, status
        except Exception as e:
            logging.error(f"Error getting CPU usage: {e}")
            return 0, "ERROR"
    
    def get_memory_usage(self) -> Tuple[float, float, float, str]:
        """Get memory usage with status indicator"""
        try:
            memory = psutil.virtual_memory()
            total_gb = round(memory.total / (1024 ** 3), 2)
            used_gb = round(memory.used / (1024 ** 3), 2)
            percent = memory.percent
            
            status = "NORMAL"
            if percent > self.thresholds['memory_critical']:
                status = "CRITICAL"
            elif percent > self.thresholds['memory_warning']:
                status = "WARNING"
                
            return total_gb, used_gb, percent, status
        except Exception as e:
            logging.error(f"Error getting memory usage: {e}")
            return 0, 0, 0, "ERROR"
    
    def get_disk_usage(self) -> List[Dict]:
        """Get disk usage for all partitions"""
        disk_info = []
        try:
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    status = "NORMAL"
                    if usage.percent > self.thresholds['disk_critical']:
                        status = "CRITICAL"
                    elif usage.percent > self.thresholds['disk_warning']:
                        status = "WARNING"
                    
                    disk_info.append({
                        'device': partition.device,
                        'mountpoint': partition.mountpoint,
                        'total_gb': round(usage.total / (1024 ** 3), 2),
                        'used_gb': round(usage.used / (1024 ** 3), 2),
                        'percent': usage.percent,
                        'status': status
                    })
                except PermissionError:
                    # Skip directories that require special permissions
                    continue
        except Exception as e:
            logging.error(f"Error getting disk usage: {e}")
        
        return disk_info
    
    def get_network_usage(self) -> Dict:
        """Get network I/O statistics"""
        try:
            net_io = psutil.net_io_counters()
            return {
                'bytes_sent': net_io.bytes_sent,
                'bytes_recv': net_io.bytes_recv,
                'packets_sent': net_io.packets_sent,
                'packets_recv': net_io.packets_recv
            }
        except Exception as e:
            logging.error(f"Error getting network usage: {e}")
            return {}
    
    def get_temperature(self) -> Tuple[float, str]:
        """Get system temperature if available"""
        try:
            # Try to get temperature information
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
                if temps:
                    for name, entries in temps.items():
                        for entry in entries:
                            if entry.current > 0:
                                status = "NORMAL"
                                if entry.current > self.thresholds['temp_critical']:
                                    status = "CRITICAL"
                                elif entry.current > self.thresholds['temp_warning']:
                                    status = "WARNING"
                                return entry.current, status
            return 0.0, "UNAVAILABLE"
        except Exception as e:
            logging.error(f"Error getting temperature: {e}")
            return 0.0, "ERROR"
    
    def get_running_processes(self, limit=10) -> List[Dict]:
        """Get top processes by CPU usage"""
        processes = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        except Exception as e:
            logging.error(f"Error getting processes: {e}")
        
        # Sort by CPU usage and return top N
        processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
        return processes[:limit]
    
    def format_bytes(self, bytes_value: int) -> str:
        """Convert bytes to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.2f} PB"
    
    def display_dashboard(self):
        """Display the system health dashboard"""
        # Get system data
        system_info = self.get_system_info()
        cpu_percent, cpu_status = self.get_cpu_usage()
        memory_total, memory_used, memory_percent, memory_status = self.get_memory_usage()
        disk_info = self.get_disk_usage()
        network_usage = self.get_network_usage()
        temperature, temp_status = self.get_temperature()
        top_processes = self.get_running_processes()
        
        # Clear screen (works on both Unix and Windows)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Display header
        print("=" * 80)
        print("SYSTEM HEALTH MONITORING DASHBOARD".center(80))
        print("Designed for Data Center Technician Role".center(80))
        print("=" * 80)
        print(f"Last update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        # System information
        print("\nSYSTEM INFORMATION:")
        print(f"  Hostname: {system_info.get('hostname', 'N/A')}")
        print(f"  OS: {system_info.get('os', 'N/A')}")
        print(f"  Processor: {system_info.get('processor', 'N/A')}")
        print(f"  Boot Time: {system_info.get('boot_time', 'N/A')}")
        print(f"  Uptime: {system_info.get('uptime', 'N/A')}")
        
        # CPU usage
        print(f"\nCPU USAGE: {cpu_percent}% [{cpu_status}]")
        bar_length = 20
        filled = int(bar_length * cpu_percent / 100)
        bar = "[" + "=" * filled + " " * (bar_length - filled) + "]"
        print(f"  {bar}")
        
        # Memory usage
        print(f"\nMEMORY USAGE: {memory_percent}% [{memory_status}]")
        print(f"  Used: {memory_used} GB / {memory_total} GB")
        filled = int(bar_length * memory_percent / 100)
        bar = "[" + "=" * filled + " " * (bar_length - filled) + "]"
        print(f"  {bar}")
        
        # Disk usage
        print("\nDISK USAGE:")
        for disk in disk_info:
            print(f"  {disk['device']} ({disk['mountpoint']}): {disk['percent']}% [{disk['status']}]")
            print(f"    Used: {disk['used_gb']} GB / {disk['total_gb']} GB")
            filled = int(bar_length * disk['percent'] / 100)
            bar = "  [" + "=" * filled + " " * (bar_length - filled) + "]"
            print(bar)
        
        # Network usage
        print("\nNETWORK USAGE:")
        print(f"  Sent: {self.format_bytes(network_usage.get('bytes_sent', 0))}")
        print(f"  Received: {self.format_bytes(network_usage.get('bytes_recv', 0))}")
        print(f"  Packets Sent: {network_usage.get('packets_sent', 0)}")
        print(f"  Packets Received: {network_usage.get('packets_recv', 0)}")
        
        # Temperature
        print(f"\nTEMPERATURE: {temperature}°C [{temp_status}]")
        
        # Top processes
        print("\nTOP PROCESSES BY CPU USAGE:")
        print("  PID     CPU%    MEM%    Name")
        for proc in top_processes:
            print(f"  {proc['pid']:6} {proc['cpu_percent']:6.1f} {proc['memory_percent']:6.1f}    {proc['name']}")
        
        print("\n" + "=" * 80)
        print("Press Ctrl+C to exit".center(80))
        print("=" * 80)
        
        # Log the current status
        logging.info(
            f"CPU: {cpu_percent}% [{cpu_status}], "
            f"Memory: {memory_percent}% [{memory_status}], "
            f"Temperature: {temperature}°C [{temp_status}]"
        )

    def run(self):
        """Run the dashboard"""
        print("Starting System Health Monitoring Dashboard...")
        print("Press Ctrl+C to exit\n")
        time.sleep(2)
        
        try:
            while True:
                self.display_dashboard()
                time.sleep(self.refresh_interval)
        except KeyboardInterrupt:
            print("\nExiting System Health Monitoring Dashboard. Goodbye!")

if __name__ == "__main__":
    dashboard = SystemHealthDashboard(refresh_interval=5)
    dashboard.run()