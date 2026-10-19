# Vanguard X – Cybersecurity Lab

## About the Project

Vanguard X is a personal cybersecurity project I'm working on to gain more practical experience in cybersecurity. I'm using Kali Linux and Metasploitable 2 to learn how to find security weaknesses, investigate vulnerable services, and understand how these issues can be fixed.

I'm also using Python to automate some security tasks, analyse logs, and detect suspicious activity.

The project is still in progress, and I'm documenting what I do as I move through each phase.

## Lab Setup

These are the main tools I'm using for the project:

* **Kali Linux** – for security testing and running Python scripts.
* **Metasploitable 2** – an intentionally vulnerable machine for practice.
* **VirtualBox** – to run the virtual machines.
* **Nmap** – to scan for open ports and identify services.
* **Python 3** – to automate security checks and analyse data.

I configured a host-only network so Kali and Metasploitable can communicate in an isolated lab environment.

## Project Progress

### Phase 1: Lab Setup — Completed

* Installed and configured Kali Linux.
* Set up Metasploitable 2 in VirtualBox.
* Configured the host-only network.
* Tested the connection between both machines.
* Documented the lab setup with screenshots.

### Phase 2: Reconnaissance and Enumeration — Completed

I used Nmap and other tools to investigate the Metasploitable machine.

What I did:

* Scanned for open ports.
* Identified running services and their versions.
* Checked the available web services.
* Looked at HTTP response headers.
* Investigated the web applications running on the target.
* Recorded services that need further vulnerability investigation.

Some of the services I found included FTP, SSH, Telnet, HTTP, MySQL, and Tomcat. Finding an old service version does not automatically confirm a vulnerability, so I'll investigate these findings further in the next phase.

### Phase 3: Python for Security — Initial Exercises Completed

For this phase, I used Python to practise automating security tasks instead of relying entirely on manual checks.

Some of the things I've worked on include:

* Using sockets to test network connections.
* Automating Nmap scans.
* Sending HTTP requests and checking server responses.
* Extracting page titles and server information.
* Checking HTTP methods and response headers.
* Examining cookies and basic session behaviour.
* Working with JSON and CSV files to store security findings.
* Using regular expressions to extract information from text.
* Filtering security findings by service.
* Analysing authentication logs.
* Counting failed login attempts from different IP addresses.
* Generating alerts when an IP reaches a specified number of failed attempts.
* Checking log entries against a list of test indicators of compromise (IOCs).

I also created sample authentication logs to test the log analysis and detection scripts.

These exercises helped me understand how Python can be used for basic security automation and defensive monitoring. I still plan to improve and integrate some of the scripts as the project continues.

## Python Scripts

The scripts for this phase are stored in the `python-security/` directory.

| File                       | What it does                                      |
| -------------------------- | ------------------------------------------------- |
| `nmap-python.py`           | Automates Nmap scanning tasks                     |
| `socket-test.py`           | Tests TCP connections using Python sockets        |
| `banner-test.py`           | Practises retrieving service banners              |
| `web-request.py`           | Sends HTTP requests                               |
| `http_methods.py`          | Checks HTTP method behaviour                      |
| `http_method_checker.py`   | Performs additional HTTP method checks            |
| `cookie_check.py`          | Checks cookie behaviour                           |
| `cookie_secuirty_check.py` | Performs cookie security checks                   |
| `session_check.py`         | Tests basic session behaviour                     |
| `regex.py`                 | Practises regular expressions                     |
| `csv_processing.py`        | Reads and processes CSV security findings         |
| `filter_findings.py`       | Filters security findings                         |
| `log_analyzer.py`          | Counts failed login attempts and generates alerts |
| `ioc_detector.py`          | Checks logs against test IOC indicators           |

Other files in the directory include the Nmap results, security findings in JSON and CSV formats, and the sample authentication log.

The IP addresses used in the sample logs and IOC exercises are test data. They have not been confirmed to be malicious.

## What's Next?

### Phase 4: Vulnerability Assessment

Next, I plan to investigate the services discovered during reconnaissance and determine which ones have actual security weaknesses.

I'll work on:

* Researching potential vulnerabilities.
* Verifying findings in the lab.
* Performing controlled tests against vulnerable services.
* Recording evidence and possible impact.
* Learning how to fix identified weaknesses and retest them.

### Phase 5: Web Application Security

I'll use intentionally vulnerable web applications to practise identifying issues such as:

* SQL injection.
* Cross-site scripting (XSS).
* Authentication and session weaknesses.
* Access control problems.
* File inclusion vulnerabilities.

I'll also use tools such as Burp Suite or OWASP ZAP to inspect web requests and responses.

### Phase 6: Linux Security

I'll investigate Linux permissions, users, services, and insecure configurations, then practise applying security improvements.

### Phase 7: Network Security

I'll explore insecure network services, analyse selected traffic with Wireshark, and learn more about network security controls.

### Phase 8: Blue Team and SOC

I'll continue building on the Python log analysis exercises by working on suspicious activity detection, IOC matching, basic alerting, and defensive automation. I'll also learn more about SIEM tools and how security events are monitored.

### Phase 9: Final Assessment

At the end of the project, I'll bring the different parts together, document the findings, recommend fixes, and retest the relevant issues.

## Repository Structure

```text
vanguard-x/
├── docs/
│   └── lab-architecture.md
├── reconnaissance/
│   └── findings.md
├── python-security/
│   ├── nmap-python.py
│   ├── socket-test.py
│   ├── banner-test.py
│   ├── web-request.py
│   ├── http_methods.py
│   ├── http_method_checker.py
│   ├── cookie_check.py
│   ├── cookie_secuirty_check.py
│   ├── session_check.py
│   ├── regex.py
│   ├── csv_processing.py
│   ├── filter_findings.py
│   ├── log_analyzer.py
│   ├── ioc_detector.py
│   ├── nmap-results.json
│   ├── security-findings.json
│   ├── security-findings.csv
│   └── sample_auth.log
└── screenshots/
```

## Running the Python Scripts

Clone the repository:

```bash
git clone https://github.com/Chibueze2007/vanguard-x.git
cd vanguard-x
```

To run the log analyzer:

```bash
cd python-security
python3 log_analyzer.py
```

To run the IOC detector:

```bash
python3 ioc_detector.py
```

Both scripts use the sample authentication log in the same directory.

## Safety

All testing is carried out in my own lab using intentionally vulnerable machines and applications. I won't test systems without permission.

## Final Note

I'm building Vanguard X to improve my practical cybersecurity skills and understand how offensive security, Python automation, and defensive monitoring work together. I'll keep updating the repository as I complete more exercises and add new findings.

