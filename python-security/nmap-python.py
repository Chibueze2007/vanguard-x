import subprocess
import json
result = subprocess.run(["nmap", "-sV", "192.168.56.104"], capture_output= True, text =True)
services = []
for line in result.stdout.splitlines():
     if "open" in line:
        parts = line.split()
        port = parts[0]
        state = parts[1]
        service = parts[2]
        version = " ".join(parts[3:])
        if not version:
            version = "Undetected"
        services.append({
            "port": port,
            "state": state,
            "service": service,
            "version": version
        })
        print(f"====={service}=====")
        print(f"Port {port}:\nState:{state}\nService: {service}\nVersion: {version}")

for s in services:
       if s["service"] =="http":
        print(f"{s['service']} is running on port {s['port']} with version {s['version']}")
       if "vsftpd 2.3.4" in s["version"]:
        print(f"Investigation needed: {s['service']} on port {s['port']}")
with open("nmap-results.json","w") as file:
    json.dump(services,file,indent=4)
with open("nmap-results.json","r") as file:
    saved_services = json.load(file)
print(saved_services)
interesting_services = ["http", "ftp"]
findings = []
for service in saved_services:
    if service["service"] in interesting_services:
        findings.append({
            "port": service["port"],
            "service": service["service"],
            "version": service["version"],
            "status": "Investigation needed"
        })
        print(
            f"Service detetcted: {service['service']} -"
            f"{service['port']} - {service['version']} - Investigation needed"
        )
print(findings)	

with open("security-findings.json", "w") as file:
    json.dump(findings, file, indent=4)
