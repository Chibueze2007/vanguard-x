# Vanguard X — Reconnaissance Findings

## 1. Introduction

The reconnaissance phase of Vanguard X was carried out to find out what services were running on the Metasploitable 2 machine and to get a better understanding of the target before performing further security testing.

The target used for this phase was:

`192.168.56.104`

The scan was performed from the Kali Linux machine on the isolated Vanguard X network.

## 2. Initial Nmap Scan

I started with a basic Nmap scan:

```bash
nmap 192.168.56.104
```

The scan showed that the target was online and had several open TCP ports.

Some of the services found included:

* FTP
* SSH
* Telnet
* SMTP
* DNS
* HTTP
* SMB
* NFS
* MySQL
* PostgreSQL
* VNC
* IRC
* Apache Tomcat

In total, 22 open TCP ports were identified by the scan.

## 3. Service and Version Detection

After finding the open ports, I used Nmap's service and version detection:

```bash
nmap -sV 192.168.56.104
```

This gave more information about the software running on the different ports.

| Port | Service    | Detected Software          |
| ---: | ---------- | -------------------------- |
|   21 | FTP        | vsftpd 2.3.4               |
|   22 | SSH        | OpenSSH 4.7p1              |
|   23 | Telnet     | Linux telnetd              |
|   25 | SMTP       | Postfix smtpd              |
|   53 | DNS        | ISC BIND 9.4.2             |
|   80 | HTTP       | Apache 2.2.8               |
|  111 | RPCbind    | RPC                        |
|  139 | NetBIOS    | Samba                      |
|  445 | SMB        | Samba                      |
|  512 | exec       | rexecd                     |
|  513 | login      | rlogind                    |
|  514 | shell      | rshd                       |
| 1099 | Java RMI   | GNU Classpath grmiregistry |
| 1524 | Bindshell  | Metasploitable root shell  |
| 2049 | NFS        | NFS v2–4                   |
| 2121 | FTP        | ProFTPD 1.3.1              |
| 3306 | MySQL      | MySQL 5.0.51a              |
| 5432 | PostgreSQL | PostgreSQL 8.3.x           |
| 5900 | VNC        | VNC                        |
| 6000 | X11        | X11                        |
| 6667 | IRC        | UnrealIRCd                 |
| 8009 | AJP        | Apache JServ Protocol      |
| 8180 | HTTP       | Apache Tomcat              |

## 4. What I Observed

The main thing I noticed from the scans was that Metasploitable 2 has a large number of services running at the same time.

There are also several older software versions. For example, the target is running vsftpd 2.3.4, Apache 2.2.8, ProFTPD 1.3.1, MySQL 5.0.51a and other older services.

This gives me several areas to investigate further.

However, finding an old version does not automatically mean that the service is vulnerable. I need to investigate the individual services and verify any vulnerabilities in the lab before considering them findings.

Another interesting discovery was port `1524`, which Nmap identified as a Metasploitable root shell. This will be investigated later as part of the controlled exploitation phase.

## 5. Evidence

The following screenshots were captured during the reconnaissance phase:

* `03-initial-nmap-scan.png` — Initial Nmap scan
* `04-nmap-service-version-scan.png` — Service and version detection

## 6. Next Step

The next step is to perform more detailed enumeration of selected services.

I will start with the HTTP services because the target has web services running on ports `80` and `8180`.

The goal will be to identify the web applications, technologies, directories, and other information that can help with the later security assessment.
