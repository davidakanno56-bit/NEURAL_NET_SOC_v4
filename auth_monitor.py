import re
from datetime import datetime

# Path to system authentication log file
LOG_FILE = "/var/log/auth.log"

# Threshold for triggering a security alert
FAILED_ATTEMPT_LIMIT = 3

def parse_auth_logs():
    failed_attempts = {}
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting NEURAL_NET Log Scan...")

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                # Check for failed password attempts
                if "Failed password" in line:
                    # Extract IP address using Regex
                    ip_match = re.search(r'from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        print("\n--- SCAN RESULTS ---")
        for ip, count in failed_attempts.items():
            if count >= FAILED_ATTEMPT_LIMIT:
                print(f"[🚨 ALERT] Potential Brute-Force Attack from IP: {ip} | Failed Attempts: {count}")
            else:
                print(f"[ℹ️ INFO] IP: {ip} | Failed Attempts: {count}")

    except FileNotFoundError:
        print(f"[❌ ERROR] Could not find log file at {LOG_FILE}. Run script on Ubuntu target host.")

if __name__ == "__main__":
    parse_auth_logs()
