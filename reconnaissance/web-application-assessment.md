# Vanguard X – Web Application Assessment

## 1. Assessment Overview

**Project:** Vanguard X  
**Target:** Metasploitable 2  
**Target IP:** 192.168.56.104  
**Assessment Type:** Web Application Vulnerability Assessment  
**Environment:** Isolated VirtualBox Lab  

## 2. Applications Identified

### 2.1 DVWA (Damn Vulnerable Web Application)

- URL: http://192.168.56.104/dvwa/
- Accessibility: Accessible
- Login: Successful
- Security Level: High

Observation:
The DVWA application loaded successfully, and I was able to access its dashboard. The security level was set to High during the initial assessment.

### 2.2 Mutillidae

- URL: http://192.168.56.104/mutillidae/
- Accessibility: Accessible

Observation:
The Mutillidae application loaded successfully in the browser. Further security testing has not yet been performed.

### 2.3 phpMyAdmin

- URL: http://192.168.56.104/phpmyadmin/
- Accessibility: Accessible
- Login Page: Displayed

Observation:
The phpMyAdmin login page was accessible. Authentication and version identification have not yet been assessed.

### 2.4 TWiki

- URL: To be confirmed
- Accessibility: Previously identified during reconnaissance.

Observation:
TWiki was discovered during the initial web enumeration. Further assessment is pending.

### 2.5 Apache Tomcat

- Port: 8180
- Service: Apache Tomcat
- Initial Observation: The manager interface returned HTTP 401 (Unauthorized).

Observation:
The Tomcat manager interface requires authentication. No authentication testing has been performed.

## 3. Initial Assessment Summary

Several web applications and services are accessible on the Metasploitable 2 target.

At this stage, accessibility has been confirmed, but specific vulnerabilities have not yet been established in these applications.

## 4. Next Steps

1. Identify the phpMyAdmin version.
2. Investigate the exposed web applications.
3. Assess authentication and access controls.
4. Perform controlled vulnerability testing.
5. Document confirmed findings and recommendations.

## 5. Evidence

Screenshots will be stored in the Vanguard X screenshots directory.