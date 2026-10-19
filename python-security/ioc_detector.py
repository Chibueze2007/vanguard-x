suspicious_ips = ["192.168.56.20", "10.10.10.50"]
log_file = "sample_auth.log"

with open(log_file, "r") as file:
    for line in file:
        for ip in suspicious_ips:
            if ip in line:
                print(f"Suspicious activity detected from IP: {ip}")
                print(f"Log entry: {line.strip()}")
