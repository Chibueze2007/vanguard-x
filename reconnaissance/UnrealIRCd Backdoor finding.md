**Vulnerability:** UnrealIRCd 3.2.8.1 Backdoor  
**CVE:** CVE-2010-2075  
**Target:** 192.168.56.104  
**Port:** 6667/TCP  
**Severity:** Critical  
**Status:** Confirmed and successfully exploited.  
**Access Obtained** Root

**Description:**

The UnrealIRCd installation contained a backdoor that allowed remote command execution without normal authentication.

**Evidence:**

- Nmap detected a trojaned UnrealIRCd version.
- Metasploit confirmed that the target was vulnerable.
- A Meterpreter session was successfully established.
- The `getuid` command returned `root`.
- The `sysinfo` command identified Ubuntu 8.04.

**Impact:**

An attacker could obtain root-level access and potentially take complete control of the affected system.

**Recommendation:**

Remove the compromised installation and replace it with a trusted, verified version. Restrict access to the IRC service.