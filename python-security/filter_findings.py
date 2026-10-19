import csv
with open("security-findings.csv","r") as file:
    reader = csv.DictReader(file)
    for finding in reader:
        if finding["service"] =="HTTP":
            print(finding)
