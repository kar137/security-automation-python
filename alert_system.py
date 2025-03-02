import re

def monitor_logs(log_file):
    # suspicious patterns
    suspicious_patterns = [
        "failed login",
        "unauthorized access",
        "malicious activity detected"
    ]
    
    try:
        with open(log_file, "r") as file:  # opening file with file handling
            for line in file:
                for pattern in suspicious_patterns:
                    if re.search(pattern, line, re.IGNORECASE):  # search line by line for regex pattern ignoring letter case
                        timestamp = extract_timestamp(line)  #passes this to extract_timestamp function
                        alert_message = f"ALERT: {pattern.upper()} DETECTED AT {timestamp}"
                        print(alert_message)
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred while processing the log file: {e}")

def extract_timestamp(log_line):
    # example for timestamps like [2024-12-22 10:45:00]
    timestamp_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
    match = re.search(timestamp_pattern, log_line)  # search for regex pattern in log_logline
    return match.group(1) if match else "UNKNOWN TIME"   # match.group(1) extracts the content of the first capturing group which is timestamp_pattern

# example usage
log_file_path = "greentick/system_logs.txt"  
monitor_logs(log_file_path)