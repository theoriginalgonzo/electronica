# Password Auditing with John the Ripper (Kali Linux)
## Purpose of John the Ripper

John the Ripper (JtR) is an offline password auditing tool used to evaluate password strength by attempting to recover plaintext passwords from known password hashes.

It is important to note that John the Ripper does not attack live systems. It only operates on password hashes that are already obtained.

## Verifying John the Ripper in Kali Linux

Kali Linux includes the Jumbo version of John the Ripper by default.

To verify installation use the follow command:

```john --version```

You should see output like this:

John the Ripper 1.9.0-jumbo


The Jumbo version supports many common hash types, including:

NTLM

bcrypt

yescrypt

ZIP and RAR archives

Network device hashes

## Common Hash Sources in Lab Environments
### Linux Password Hashes

/etc/shadow

Often combined with /etc/passwd using:

unshadow passwd shadow > hashes.txt

### Windows / Active Directory (NCL-style)

NTLM hashes

Dumped using authorized lab tools

Files and Applications

ZIP, RAR, and PDF password hashes

Application or database credential stores

## Identifying Hash Types

Before cracking, the hash format should be identified.

List supported formats with the following command:

``` john --list=formats | less ```


You can also let John auto-detect the format:

john hashes.txt


Explicitly setting the format (recommended in competitions):

```john --format=NT hashes.txt```

## Wordlist-Based Password Auditing
### Why Wordlists Work

Most users:

Reuse passwords

Follow predictable patterns

Choose common words with minor variations

Wordlists simulate real user behavior and are effective for password audits.

## Common Wordlists in Kali Linux
### SecLists (Recommended)

SecLists is installed by default in Kali Linux:

/usr/share/seclists/


Common password lists:

/usr/share/seclists/Passwords/Common-Credentials/


Examples:

10-million-password-list-top-100.txt

10-million-password-list-top-500.txt

10-million-password-list-top-1000.txt

These lists are acceptable for academic reports.

rockyou.txt

Location:

/usr/share/wordlists/rockyou.txt.gz


Unzip the file:

gunzip /usr/share/wordlists/rockyou.txt.gz


This wordlist is based on a real-world breach and is useful for demonstrating weak password policies.

## Running John the Ripper with a Wordlist

Basic wordlist attack:

john --wordlist=/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-500.txt hashes.txt


View cracked passwords:

john --show hashes.txt

## Rules-Based Attacks

Rules modify passwords automatically, for example:

password → Password

password → password123

password → P@ssw0rd

Enable default rules:

john --wordlist=rockyou.txt --rules hashes.txt


Most real-world password cracks occur during rules-based attacks.

## Incremental (Brute Force) Mode

Incremental mode is used when:

Passwords are short

Wordlists fail

Command:

john --incremental hashes.txt


Against modern hash types such as bcrypt or yescrypt, brute-force attacks are intentionally slow.

## Checking Progress and Results

Show cracking status:

john --status


Show cracked passwords:

john --show hashes.txt


Cracked passwords are stored in:

~/.john/john.pot

## Interpreting Results
High-Risk Indicators

Passwords cracked in seconds

Use of top-500 passwords

Password reuse across multiple users

Weak hash algorithms (MD5, SHA-1)

Strong Security Indicators

Long passphrases

bcrypt or yescrypt hashes

No successful wordlist matches

Findings should be tied to:

Password policy recommendations

Multi-factor authentication (MFA)

Hash algorithm upgrades

## John the Ripper vs Hashcat

John the Ripper: Better for labs, auto-detection, built-in rules

Hashcat: Faster, GPU-based, more complex setup

For NCL and coursework, John the Ripper is sufficient.

## GPU Acceleration and Hashcat (RTX 3070)

An NVIDIA RTX 3070 is a good GPU for running Hashcat.

Performance Comparison

Hashcat is designed for GPU acceleration and benefits from parallel processing. On GPUs like the RTX 3070, Hashcat can perform significantly more hash attempts per second than CPU-only tools. For fast hashes such as NTLM and MD5, speed improvements can be orders of magnitude faster than CPU-based cracking.

John the Ripper is primarily CPU-focused. While the Jumbo version supports GPU acceleration, Hashcat is more optimized for GPU workloads.

Limitations

For slow or memory-hard hashes (bcrypt, scrypt, yescrypt), GPU advantages are reduced. These algorithms are designed to resist massive parallel cracking.

Summary

Using a GPU such as the NVIDIA RTX 3070 with Hashcat provides significantly higher password cracking throughput compared to CPU-only tools like John the Ripper. The advantage is greatest for fast hash types, while intentionally slow hashes reduce GPU efficiency but still benefit from acceleration.

If you paste only that content into a .md file, it will render correctly as one single Markdown document.
If you want, I can also format it to GitHub Markdown, Obsidian, or Canvas LMS exactly.

## Gym Excercise - Pokemon hashes

a532443f3e04a9e00295a8cd2a75e080:golduck
54c10b9736b70e75c6e505f340b6e2f1:basculin
b8a24794813a47521b4be55747e0665a:rotom
83b020b0a7b3c353e1c11b1647b53cda:celebi
999cae1e22fe69d89d6f56e3050f18cb:goldeen

