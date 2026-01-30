# PGP/GPG Quick Guide (NCL Prep – Week 1: OSI)

Course: Competitive Cybersecurity (CEG‑3900)

## Outline

- What PGP/GPG and how it works
- Signature and Web of Trust
- Uses and Useful commands

---

### 1. What are PGP and GPG?

- **PGP (Pretty Good Privacy)** is a standard for encrypting, signing, and verifying data using public‑key cryptography.
- **GPG (GNU Privacy Guard)** is the open‑source implementation of the OpenPGP standard and is what you’ll actually use on Linux/Windows/macOS.

### Encryption

- Sender encrypts data using the recipient’s public key
- Only the recipient can decrypt it using their private key

---

### 2. Signatures and the Web of Trust

#### Digital Signatures

A digital signature proves:

- **Who sent the data** (authentication)
- **Data was not modified** (integrity)

How it works:

1. Sender signs data using their **private key**
2. Receiver verifies the signature using the sender’s **public key**

#### Web of Trust

- PGP does **not** rely on a central authority
- Users **sign each other’s public keys** to confirm identity
- Trust is built through people verifying keys

In competitions, this often appears as:

- Verifying whether a key or file can be trusted
- Checking fingerprints and signatures

---

### 3. Uses and Useful commands

In cyber competitions, GPG commonly appears in:

- Encrypting files or messages
- Verifying file authenticity
- Signing files to prove authorship
- Importing and exporting public keys

#### Useful File Types

- `.asc` → ASCII‑armored (readable text)
- `.gpg` → binary encrypted file
- `.sig` → detached signature

### Essential Commands

- Generate a key pair:`gpg --full-generate-key`
- List keys: `gpg --list-key` `sgpg --list-secret-keys`
- Export a public key: `gpg --armor --export email@gmail.com > publickey.asc`
- Import a public key: `gpg --import publickey.asc` Encrypt a file:`gpg --encrypt -r email@gmail.com file.txt`
- Decrypt a file: `gpg --decrypt file.txt.gpg`
- Sign a file:`gpg --sign file.txt`
- Verify a signature: `gpg --verify file.txt.sig file.txt`

---
