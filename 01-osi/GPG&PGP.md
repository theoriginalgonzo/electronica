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
