# Threat Intel

## CVE and CPE

In cybersecurity, CVE and CPE are standardized naming systems used to automate the identification and management of security risks. CVE is basically what the problem is and CPE is where the problem exists, in terms of platforms or operating systems. 

The goal of CVE is the identify a security vulnerability while the CPE is to identify the produce, such as the OS, the specific hardware or an application.

CVE tracks the vulnerability itself while the CPE tracks the software or hardware versions.

## How to use CVE and CPE together

The National Vulnerability Database links these two systems together.  When new CVEs are published they are linked to specific CPEs making it easier for tools like Nmap or Tenable Nessus to identify them in a product that has that vulnerability.  

## Where it's useful in NCL

The NCL competition is designed around the CompTIA Security+ and NIST NICE frameworks, where vulnerability research is an essential skill to know. The are especially useful in the following topics. 

## Scanning & Reconnaissance: 
When you use a tool like Nmap to scan a target, it may return a version number for a service like vsftpd 2.3.4. To solve challenges, you'll need to take that information and search for a corresponding CVE to see if it is exploitable.

## Exploitation: 
Challenges often provide a specific environment or software version. Using a CPE string allows you to search the NVD (National Vulnerability Database) or CVE.org precisely to find the exact exploit needed to bypass security measures.

## Log Analysis & Forensics:
You might find a trace of an attack in a log file. Recognizing a CVE ID in a log entry helps you identify what specific exploit a "hacker" used against the system.  Many times, knowing this is key to the objective.

## GYM answers:
The CVE of the original POODLE attack: CVE-2014-3566.

VSFTPD version with the smiley face backdoor: vsftpd version 2.3.4.

First OpenSSL 1.0.1 version NOT vulnerable to Heartbleed: OpenSSL 1.0.1g.

Original RFC number for Telnet: RFC 15 (published in 1969), though it was later formalized in RFC 854.

Size of the SQL Slammer worm: 376 bytes.

Samy is my…: hero. (This was the phrase the Samy worm forced onto the profiles of over one million MySpace users).  
