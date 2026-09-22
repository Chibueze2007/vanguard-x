# Vanguard X — Lab Architecture

## 1. Overview

Vanguard X is an isolated cybersecurity assessment and defense laboratory designed for authorized security testing, vulnerability assessment, controlled exploitation, remediation, and security analysis.

All security testing is performed against intentionally vulnerable systems within the isolated laboratory environment.

## 2. Lab Components

| System           | Role                                      | Network         |
| ---------------- | ----------------------------------------- | --------------- |
| Kali Linux       | Security testing and analysis workstation | NAT + Host-Only |
| Metasploitable 2 | Intentionally vulnerable target           | Host-Only       |

## 3. Network Architecture

```text
                    Internet
                       |
                      NAT
                       |
                 +-----------+
                 |    Kali   |
                 |           |
                 | eth0      | 10.0.2.15
                 | eth1      | 192.168.56.105
                 +-----+-----+
                       |
                Host-Only Network
                192.168.56.0/24
                       |
                +------+------+
                |             |
                | Metasploitable 2
                | 192.168.56.104
                +-------------+
```

## 4. Network Configuration

### Kali Linux

* NAT interface: `10.0.2.15/24`
* Host-Only interface: `192.168.56.105/24`

### Metasploitable 2

* Host-Only interface: `192.168.56.104/24`

### Host-Only Network

* Network: `192.168.56.0/24`
* Host address: `192.168.56.1`
* DHCP: Enabled
* Purpose: Isolated communication between laboratory systems

## 5. Isolation

The vulnerable target is connected to the VirtualBox Host-Only network rather than directly to the external network.

Kali uses its NAT interface for internet connectivity and its Host-Only interface for communication with laboratory targets.

This separation allows security testing to be performed within the controlled Vanguard X environment.

## 6. Connectivity Verification

Connectivity between Kali and Metasploitable 2 was verified using ICMP.

Kali successfully reached:

`192.168.56.104`

The test produced:

* 4 packets transmitted
* 4 packets received
* 0% packet loss

## 7. Security Scope

Testing within Vanguard X is restricted to systems intentionally created or configured for this laboratory.

No unauthorized systems, networks, applications, or infrastructure will be tested.

## 8. Evidence

Screenshots documenting the initial laboratory configuration will be maintained in the project's `screenshots/` directory.

## 9. Lab Setup Status

The initial Vanguard X laboratory environment has been successfully established. Kali Linux and Metasploitable 2 are operational and connected through an isolated Host-Only network.

Network connectivity between the security workstation and vulnerable target has been verified successfully.

Additional vulnerable web applications and targets will be integrated into the laboratory during subsequent phases of the project.
