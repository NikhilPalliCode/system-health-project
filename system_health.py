"""
System Health Monitor
Simple monitoring with CPU, Memory, Disk, and Network metrics
"""

import psutil
import time
from datetime import datetime
import argparse

class SystemMonitor:
    def __init__(self, log_file="system_health.log"):
        self.log_file = log_file
        self.prev_net_io = psutil.net_io_counters()  # Store previous network stats
        self.setup_log()
    
    def setup_log(self):
        """Simple log setup"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"System Check at {datetime.now()}\n")
    
    def log(self, message):
        """Log to file and print"""
        print(message)
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"{message}\n")
    
    def get_cpu(self):
        """Get CPU metrics"""
        cpu = psutil.cpu_percent(interval=0.5)
        cores = psutil.cpu_count()
        return cpu, cores
    
    def get_memory(self):
        """Get Memory metrics"""
        mem = psutil.virtual_memory()
        total = round(mem.total / (1024**3), 2)
        used = round(mem.used / (1024**3), 2)
        percent = mem.percent
        return total, used, percent
    
    def get_disk(self):
        """Get Disk metrics"""
        disk = psutil.disk_usage('C:\\')
        total = round(disk.total / (1024**3), 2)
        used = round(disk.used / (1024**3), 2)
        percent = disk.percent
        return total, used, percent
    
    def get_network(self):
        """Get Network metrics with per-second calculation"""
        current = psutil.net_io_counters()
        
        # Calculate bytes sent/received since last check
        bytes_sent = current.bytes_sent - self.prev_net_io.bytes_sent
        bytes_recv = current.bytes_recv - self.prev_net_io.bytes_recv
        
        # Calculate packets sent/received since last check
        packets_sent = current.packets_sent - self.prev_net_io.packets_sent
        packets_recv = current.packets_recv - self.prev_net_io.packets_recv
        
        # Store current stats for next calculation
        self.prev_net_io = current
        
        # Convert to readable format
        sent_mb = round(bytes_sent / (1024**2), 3)
        recv_mb = round(bytes_recv / (1024**2), 3)
        
        return sent_mb, recv_mb, packets_sent, packets_recv
    
    def check_alerts(self, cpu, mem, disk):
        """Check for alerts"""
        alerts = []
        if cpu > 85: alerts.append(f"CPU High: {cpu}%")
        if mem > 85: alerts.append(f"Memory High: {mem}%")
        if disk > 90: alerts.append(f"Disk High: {disk}%")
        return alerts
    
    def run_once(self):
        """Run single check"""
        # Get metrics
        cpu, cores = self.get_cpu()
        mem_total, mem_used, mem_percent = self.get_memory()
        disk_total, disk_used, disk_percent = self.get_disk()
        net_sent, net_recv, packets_sent, packets_recv = self.get_network()
        
        # Check alerts
        alerts = self.check_alerts(cpu, mem_percent, disk_percent)
        
        # Display results
        self.log(f"\n{'='*50}")
        self.log("SYSTEM HEALTH REPORT")
        self.log(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log(f"{'='*50}")
        
        self.log(f"\nCPU: {cpu}% (Cores: {cores})")
        self.log(f"Memory: {mem_used}/{mem_total} GB ({mem_percent}%)")
        self.log(f"Disk C:\\: {disk_used}/{disk_total} GB ({disk_percent}%)")
        self.log(f"Network UP: {net_sent} MB/s  DOWN: {net_recv} MB/s")
        self.log(f"Packets Sent: {packets_sent}  Received: {packets_recv}")
        
        if alerts:
            self.log(f"\n[ALERTS]")
            for alert in alerts:
                self.log(f"[!] {alert}")
        
        self.log(f"\n{'='*50}")
    
    def run_continuous(self, interval=5, duration=None):
        """Run continuous monitoring"""
        self.log(f"Starting continuous monitoring (Interval: {interval}s)")
        start = time.time()
        
        try:
            while True:
                self.run_once()
                
                if duration and (time.time() - start) > duration:
                    self.log("Monitoring completed")
                    break
                
                if interval > 0:
                    time.sleep(interval)
                    
        except KeyboardInterrupt:
            self.log("Monitoring stopped")

def main():
    parser = argparse.ArgumentParser(description="System Health Monitor")
    parser.add_argument("--once", "-o", action="store_true", 
                       help="Run once and exit")
    parser.add_argument("--interval", "-i", type=int, default=5,
                       help="Interval in seconds (default: 5)")
    parser.add_argument("--duration", "-d", type=int,
                       help="Duration in seconds")
    
    args = parser.parse_args()
    
    monitor = SystemMonitor()
    
    if args.once:
        monitor.run_once()
    else:
        monitor.run_continuous(interval=args.interval, duration=args.duration)

if __name__ == "__main__":
    main()