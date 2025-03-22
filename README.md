# security-automation-python

## Overview
This repository contains solutions for the following systems:
1. **SystemMonitor**: A log parsing and alerting system.
2. **WebScanCrawler**: A simple web crawler for vulnerability scanning.

## 1. SystemMonitor
Developed a function that reads a log file and identifies error messages or suspicious patterns such as:
- "failed login"
- "unauthorized access"
- "malicious activity detected"

If such patterns are detected, the system generates an alert.

### How to Run
```bash
python alert_system.py
```

---

## 2. WebScanCrawler
Developed a web crawler that scans a website for basic security vulnerabilities, including:
- Missing HTTP security headers.
- Outdated software versions (if visible in headers or HTML).
- Forms lacking proper security attributes.

### How to Run
```bash
python app.py
```

## Setup & Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/kar137/securitysystem-scripts-python.git
   cd securitysystem-scripts-python
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scripts as described above.

## Hosting
The live solution can be found at: [https://securitysystemcheck.onrender.com]
- Note: Wait for some minutes as it might be in sleep mode.
