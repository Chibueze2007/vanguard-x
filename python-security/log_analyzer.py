import re
failed_attempts = {}
suspicious_ips= ["192.168.56.20", "10.10.10.50"]
with open("sample_auth.log","r") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if match:
                ip = match.group()
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

for ip, count in failed_attempts.items():
    print(f"IP: {ip}, Failed Attempts: {count}")
    if count >=3:
        print(f"Suspicious activity from {ip} with {count} failed attempts.")
with open("sample_auth.log", "r") as file:
    for line in file:
        for ip in suspicious_ips:
            if ip in line:
                print(f"IOC MATCH: {ip}")
                print(f"Log entry: {line.strip()}")
