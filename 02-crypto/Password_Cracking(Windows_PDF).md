# Password Cracking (Windows & PDF)

## 0. Outline

- [1. What are hashes and password hashing?](#1-what-are-hashes-and-password-hashing)
- [2. Common Hash Types](#2-common-hash-types)
- [3. Tools for Cracking Password Hashes](#3-tools-for-cracking-password-hashes)
- [4. Cracking Windows Password Hashes](#4-cracking-windows-password-hashes)
- [5. Cracking PDF Passwords](#5-cracking-pdf-passwords)
- [6. Citations](#6-citations)

## 1. What are hashes and password hashing?

- A **hash** is a fixed-length string of characters generated from input data of any size using a mathematical function called a hash function.
- Hashes are designed to be unique, meaning that even a small change in the input data will produce a completely different hash.
- **Password hashing** is the process of converting a password into a hash using a hash function. This is done to securely store passwords, as hashes are one-way functions and cannot be easily reversed to obtain the original password.

## 2. Common Hash Types

- **MD5**: Produces a 128-bit hash value, commonly represented as a 32-character hexadecimal number. It is fast but has known vulnerabilities.
- **SHA-1**: Produces a 160-bit hash value, represented as a 40-character hexadecimal number. It is more secure than MD5 but has also been found to have vulnerabilities.
- **SHA-256**: Part of the SHA-2 family, produces a 256-bit hash value, represented as a 64-character hexadecimal number. It is widely used and considered secure.
- **NTLM**: A suite of Microsoft security protocols that includes a hashing algorithm for passwords used in Windows systems. NTLM hashes are 128-bit and represented as a 32-character hexadecimal number.

## 3. Tools for Cracking Password Hashes

- **Hashcat**: A powerful and versatile password cracking tool that supports a wide range of hash types and attack modes. It can utilize GPU acceleration for faster cracking.
- **John the Ripper**: A popular password cracking tool that supports various hash types and is known for its ease of use and effectiveness.
- **Cain & Abel**: A Windows-based password recovery tool that can crack various types of hashes, including NTLM.

## 4. Cracking Windows Password Hashes

- Windows stores password hashes in the SAM (Security Account Manager) database.
- To extract NTLM hashes from a Windows system, tools like `pwdump` or `fgdump` can be used.
- Once the hashes are extracted, they can be cracked using tools like Hashcat or John the Ripper with appropriate wordlists or brute-force methods.

## 5. Cracking PDF Passwords

- PDF files can be protected with passwords to restrict access or editing.
- Tools like `pdfcrack` or `John the Ripper` can be used to crack PDF passwords.
- The process typically involves using a wordlist or brute-force methods to guess the password and unlock the PDF file.

## 6. Citations
