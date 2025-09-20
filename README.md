# System Health Monitoring Dashboard for Data Center Operations

A comprehensive Python-based system health monitoring dashboard designed to simulate data center infrastructure monitoring protocols used by Amazon Web Services. This tool provides real-time visibility into server performance, resource utilization, and system alerts.

## 🚀 Features

- **Real-time System Monitoring**: Track CPU, memory, disk, and network metrics
- **Configurable Alerting**: Customizable thresholds with status indicators (NORMAL, WARNING, CRITICAL)
- **Temperature Monitoring**: Hardware temperature tracking with alert system
- **Process Analysis**: Identify top resource-consuming processes
- **Comprehensive Logging**: Automated logging for incident analysis and troubleshooting
- **Visual Indicators**: Progress bars and status indicators for at-a-glance health assessment

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/NikhilPalliCode/system-health-dashboard.git
cd system-health-dashboard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚦 Usage

Run the dashboard with default settings:
```bash
python system_health_dashboard.py
```

Run with custom refresh interval (in seconds):
```bash
python system_health_dashboard.py --interval 10
```

Command line options:
- `--interval`: Set refresh interval in seconds (default: 5)
- `--log-file`: Specify custom log file path
- `--no-color`: Disable colored output

## 📊 Monitored Metrics

| Metric Category | Specific Metrics | Alert Thresholds |
|----------------|------------------|------------------|
| **CPU** | Utilization percentage | Warning: 80%, Critical: 90% |
| **Memory** | Total, Used, Percentage | Warning: 75%, Critical: 85% |
| **Disk** | All partitions usage | Warning: 80%, Critical: 90% |
| **Network** | Bytes sent/received, Packets | N/A |
| **Temperature** | System sensors | Warning: 70°C, Critical: 80°C |
| **Processes** | Top 10 by CPU usage | N/A |

## ⚙️ Configuration

Modify threshold values in the code:
```python
self.thresholds = {
    'cpu_warning': 80,        # CPU usage warning threshold (%)
    'cpu_critical': 90,       # CPU usage critical threshold (%)
    'memory_warning': 75,     # Memory usage warning threshold (%)
    'memory_critical': 85,    # Memory usage critical threshold (%)
    'disk_warning': 80,       # Disk usage warning threshold (%)
    'disk_critical': 90,      # Disk usage critical threshold (%)
    'temp_warning': 70,       # Temperature warning threshold (°C)
    'temp_critical': 80       # Temperature critical threshold (°C)
}
```

## 📝 Logging

The application automatically logs system events to `system_health.log` with the following format:
```
2023-11-15 14:30:45 - INFO - CPU usage warning: 82%
2023-11-15 14:31:15 - WARNING - Memory usage critical: 87%
```

## 🧪 Testing

The dashboard includes built-in validation for:
- Sensor availability detection
- Permission handling for restricted system information
- Error handling for missing components

## 🌟 Project Highlights

This project demonstrates skills relevant to Data Center Technician roles:

- **System Architecture**: Designed a modular monitoring system with configurable components
- **Performance Optimization**: Implemented efficient polling intervals to minimize system impact
- **Alert Management**: Created threshold-based alerting system following industry standards
- **Logging & Documentation**: Built comprehensive logging for incident analysis
- **Cross-Platform Compatibility**: Ensured functionality across Linux, Windows, and macOS

## 🔧 Technical Implementation

- **Python 3.8+**: Core programming language
- **psutil library**: System and process utilities
- **platform module**: OS and hardware information
- **socket library**: Network and hostname information
- **logging module**: Comprehensive event logging
- **typing module**: Type hints for code clarity

## 📈 Sample Output

```
====================================================
            SYSTEM HEALTH MONITORING DASHBOARD
         Designed for Data Center Technician Role
====================================================
Last update: 2023-11-15 14:30:45
====================================================

SYSTEM INFORMATION:
  Hostname: server01
  OS: Linux 5.15.0-86-generic
  Processor: Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz
  Boot Time: 2023-11-14 08:15:32
  Uptime: 1 day, 6:15:13

CPU USAGE: 45.2% [NORMAL]
  [==========          ]

MEMORY USAGE: 62.3% [NORMAL]
  Used: 15.8 GB / 25.4 GB
  [==============      ]
...
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Inspired by AWS data center monitoring tools
- Built with psutil library for system information
- Designed following Amazon operational excellence principles
