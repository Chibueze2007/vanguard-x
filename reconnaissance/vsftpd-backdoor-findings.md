### VX-VA-001: vsftpd 2.3.4 Backdoor

**Target:** 192.168.56.104
**Service:** FTP
**Port:** 21/TCP
**Software:** vsftpd 2.3.4
**CVE:** CVE-2011-2523
**Severity:** Critical
**Status:** Confirmed

**Description:**

The FTP service running on the Metasploitable 2 machine was found to contain the vsftpd 2.3.4 backdoor vulnerability.

The vulnerability was investigated using Nmap's `ftp-vsftpd-backdoor` script.

**Testing command:**

`nmap -p 21 --script ftp-vsftpd-backdoor 192.168.56.104`

**Evidence:**

The Nmap script reported:

* State: VULNERABLE (Exploitable)
* CVE: CVE-2011-2523
* Shell command executed: `id`
* Result: `uid=0(root) gid=0(root)`

**Impact:**

An attacker who can reach the affected service could potentially execute commands without normal authentication and gain root-level access to the target machine.

This could allow unauthorized access to files, system configurations and other sensitive resources.

**Recommendation:**

Remove the affected vsftpd installation and replace it with a trusted, verified version obtained from an official source. Restrict FTP access to authorized users and networks, and use encrypted file transfer protocols such as SFTP.

**Conclusion:**

The vulnerability was successfully verified in the isolated lab environment. The Nmap script executed the `id` command through the backdoor and returned root-level user information.
