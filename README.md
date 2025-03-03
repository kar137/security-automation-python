# securitysystem-scripts-python

## Overview
This repository contains solutions for the Green Tick Technical Assessment. The assessment includes two tasks:
1. **SystemMonitor**: A log parsing and alerting system.
2. **WebScanCrawler**: A simple web crawler for vulnerability scanning.

## 1. SystemMonitor
### Problem Statement
Develop a function that reads a log file and identifies error messages or suspicious patterns such as:
- "failed login"
- "unauthorized access"
- "malicious activity detected"

If such patterns are detected, the system generates an alert.

### Input
A text log file containing system logs.

### Expected Output Example
```
ALERT: UNAUTHORIZED ACCESS ATTEMPT DETECTED AT 2024-12-22 10:45:00
```

### How to Run
```bash
python alert_system.py
```

### Assumptions & Limitations
- The script scans logs line by line for predefined suspicious patterns.
- It assumes logs are in plaintext format.
- No machine learning techniques are used; it's purely rule-based.

---

## 2. WebScanCrawler
### Problem Statement
Develop a web crawler that scans a website for basic security vulnerabilities, including:
- Missing HTTP security headers.
- Outdated software versions (if visible in headers or HTML).
- Forms lacking proper security attributes.

The crawler should:
1. Accept a URL to start scanning.
2. Crawl linked pages recursively.
3. Check for vulnerabilities and generate a report.

### Input
A URL to scan (e.g., `http://nabinkhadka1.com.np`).

### Expected Output Example
```
VULNERABILITY SCAN REPORT FOR http://nabinkhadka1.com.np:
- MISSING HTTP SECURITY HEADERS: STRICT-TRANSPORT-SECURITY
- OUTDATED SOFTWARE VERSION DETECTED: APACHE 2.4.6
- FORM WITHOUT PROPER METHOD ATTRIBUTE: /CONTACT-FORM
```

### How to Run
```bash
python webscancrawler.py http://nabinkhadka1.com.np
```

### Assumptions & Limitations
- The crawler follows links within the same domain.
- It does not attempt deep security testing (e.g., SQL injection, XSS detection).
- Headers and form attributes are checked based on basic heuristics.

---

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
- Note: Wait for some minutes it might be in sleep mode.

## License
This project is for assessment purposes only and does not come with any license.

---

### Author
Karan Bista
