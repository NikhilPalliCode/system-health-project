```markdown
# System Health Monitor

A lightweight, production-ready Python tool for monitoring system resources with real-time alerts and logging. Perfect for demonstrating system monitoring skills for technical roles.

## 🚀 Features

- **Real-time Monitoring**: CPU, Memory, Disk, and Network metrics
- **Smart Alerts**: Configurable thresholds with automatic alerting
- **Network Speed Calculation**: Real-time upload/download speed measurement
- **Dual Logging**: Console output + file logging
- **Flexible Operation**: Single check or continuous monitoring
- **Command-line Interface**: Easy-to-use with multiple options

## 📋 Prerequisites

- Python 3.6 or higher
- Windows, Linux, or macOS

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/NikhilPalliCode/system-health-project.git
cd system-health-project
```

2. Install required dependency:
```bash
pip install psutil
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## 🚦 Usage

### Basic Commands

**Run once and exit:**
```bash
python system_health.py --once
```

**Continuous monitoring (default: 5-second intervals):**
```bash
python system_health.py
```

**Custom interval (10 seconds):**
```bash
python system_health.py --interval 10
```

**Run for specific duration (60 seconds):**
```bash
python system_health.py --duration 60
```

**Combine options:**
```bash
python system_health.py --interval 10 --duration 120
```

## 📊 Monitored Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| **CPU Usage** | Percentage of CPU utilization | > 85% |
| **Memory Usage** | Total, Used, Available memory | > 85% |
| **Disk Usage** | C: drive usage percentage | > 90% |
| **Network Speed** | Real-time upload/download speed | N/A |
| **Network Packets** | Packets sent and received | N/A |

## ⚠️ Alert System

The monitor automatically detects and alerts on:
- **High CPU Usage**: > 85%
- **High Memory Usage**: > 85% 
- **High Disk Usage**: > 90%

## 📝 Logging

The application logs to `system_health.log` with timestamps. Example log entry:
```
==================================================
SYSTEM HEALTH REPORT
Time: 2026-01-14 13:53:46
==================================================

CPU: 24.3% (Cores: 12)
Memory: 6.74/7.31 GB (92.2%)
Disk C:\: 157.79/237.42 GB (66.5%)
Network UP: 0.125 MB/s  DOWN: 0.543 MB/s
Packets Sent: 45  Received: 128

[ALERTS]
[!] Memory High: 92.2%
==================================================
```

## 🔧 Technical Implementation

- **Python 3.6+**: Core programming language
- **psutil library**: System and process utilities
- **argparse**: Command-line interface
- **time/datetime**: Timing and timestamp management
- **Cross-platform**: Works on Windows, Linux, and macOS

## 🎯 Key Technical Features

1. **Network Speed Calculation**: Calculates real-time MB/sec by comparing network counters between intervals
2. **Clean OOP Design**: Modular, maintainable class structure
3. **Error Handling**: Graceful handling of keyboard interrupts and errors
4. **Configurable**: Adjustable intervals and monitoring duration
5. **Production-ready**: Professional logging and output formatting

## 📈 Sample Output

```
==================================================
SYSTEM HEALTH REPORT
Time: 2026-01-14 14:30:45
==================================================

CPU: 18.8% (Cores: 12)
Memory: 6.71/7.31 GB (91.7%)
Disk C:\: 157.32/237.42 GB (66.3%)
Network UP: 0.125 MB/s  DOWN: 0.543 MB/s
Packets Sent: 45  Received: 128

[ALERTS]
[!] Memory High: 91.7%
==================================================
```

## 🏗️ Project Structure

```
system_health.py          # Main Python script
requirements.txt          # Dependencies (psutil)
README.md                # This documentation
.gitignore              # Git ignore file
system_health.log       # Generated log file (not tracked)
```


```

