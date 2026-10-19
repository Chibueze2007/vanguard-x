import csv

# Sample security findings from our lab
findings = [
    {
        "port": 21,
        "service": "FTP",
        "version": "vsftpd 2.3.4",
        "status": "Investigation needed"
    },
    {
        "port": 80,
        "service": "HTTP",
        "version": "Apache 2.2.8",
        "status": "Investigation needed"
    },
    {
        "port": 2121,
        "service": "FTP",
        "version": "ProFTPD 1.3.1",
        "status": "Investigation needed"
    },
    {
        "port": 8180,
        "service": "HTTP",
        "version": "Tomcat/Coyote 1.1",
        "status": "Investigation needed"
    }
]

# Write findings to a CSV file
with open("security-findings.csv", "w", newline="") as file:
    fieldnames = ["port", "service", "version", "status"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(findings)

print("Security findings saved to security-findings.csv")

# Read the CSV file
print("\nReading security findings:")

with open("security-findings.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for finding in reader:
        print(
            f"Port: {finding['port']} | "
            f"Service: {finding['service']} | "
            f"Version: {finding['version']} | "
            f"Status: {finding['status']}"
        )

