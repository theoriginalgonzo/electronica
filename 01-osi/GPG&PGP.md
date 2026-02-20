# PGP/GPG Quick Guide

## 0. Outline

- [1. What are PGP and GPG?](#1-what-are-pgp-and-gpg)
- [2. Key Servers and Web of Trust](#2-key-servers-and-web-of-trust)
- [3. Uses and GPG in NCL](#3-uses-and-gpg-in-ncl)
- [4. Citations](#4-citations)

## 1. What are PGP and GPG?

- **PGP (Pretty Good Privacy)** is a standard for encrypting, signing, and verifying data using public‑key cryptography.
- **GPG (GNU Privacy Guard)** is the open‑source implementation of the OpenPGP standard and is what you’ll actually use on a terminal.

ㅤ

## 2. Key Servers and Web of Trust

### Key Servers

- Key servers are public servers that store and distribute public keys
- Examples: [Ubuntu keyserver](https://keyserver.ubuntu.com/), [openpgp.org](https://keys.openpgp.org/), [MIT PGP Public Key Server](https://pgp.mit.edu/)
- They help users find and share public keys

Note: Servers do not verify identity for you, as anyone can upload a public key. Trust is established by vouching for other users (i.e signing their keys) hence creating a web of trust.

### Web of Trust

Since PGP does not have a central authority, users sign each other’s public keys to confirm identity, and trust is built through people verifying each other's keys. For example: Bob, Alice, Charlie have keys, if Bob signs Alice's key, and she signs Charlie's key, Bob can be fairly confident that John is who he claims to be.

ㅤ

## 3. Uses and GPG in NCL

In cyber competitions, GPG commonly appears in:

- Checking fingerprints and identifying keys
- Importing and exporting public keys
- Signing/verifying files
- Encrypting/decrypting files or messages

### Checking fingerprints and identifying keys

A fingerprint is a unique hash (40 chars) that identifies a public key. It's more much reliable than a Key ID (last 8-16 chars of full fingerprints) or name/email and is used to compare fingerprints from a different sources and confirm the key you imported is the correct one.

Competitions might ask you to find the email associated with a fingerprint e.g

- `security@cpanel.net` -> `ded38747ceefc789fdc3a6154cf279c5c0424907`, `b6709b4cc6f42077f69841919521bedcabd94ddf`
- `7A39A56B73D1E097D57435CFCDE2DE1DCB2077F2` -> `hx@liber8tion.cityinthe.cloud`

You might also be asked to find details about the key (eg creation/expiry date)

- In the gym case the expiration date can be found in the self-signature line: `2050-12-26T20:36:17Z`

### Importing and exporting public keys

A GPG keyring is the combination of your private key and the public keys you have imported. Keys can be imported locally from downloaded files or from key servers, same for exporting.

- Import a public key from a file:`gpg --import pubkey.asc`
- Import a public key from a server:`gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys "Key ID"`
- Export your public key to a file: `gpg --export --armor "email" > mypubkey.asc`
- Export your public key to a server: `gpg --keyserver hkps://keyserver.ubuntu.com --send-keys "Key ID"`

### Signing/Verifying Files

Signing a file lets others know it really came from you and verifying checks that the signature is valid and the file hasn’t been modified.

- Sender signs data using their private key: `gpg --sign file.txt` or `gpg --detach-sign file.txt` (returns file.txt.gpg or file.txt.sig)
- Receiver verifies the signature using the sender’s public key: `gpg --verify file.txt.gpg` or `gpg --verify file.txt.sig file.txt` (returns Good/Bad signature)

### Encrypting files or messages

Encryption ensures that only the intended recipient can read the data. Decryption restores the original content using the recipient’s private key.

- You encrypt a file for Bob: `gpg --encrypt --recipient email@wright.edu file.txt`
- Bob decrypts using his private key:`gpg --decrypt file.txt.gpg`

### Common File Types

- `.asc` → ASCII‑armored (readable text)
- `.gpg` → binary encrypted file
- `.sig` → detached signature

### Other Usefull Commands

- Generate a key pair:`gpg --full-generate-key`
- List keys: `gpg --list-key` `sgpg --list-secret-keys`
- List signatures: `gpg --list-sigs`

## 4. Citations

- [What is PGP Encryption and How Does It Work?](https://www.varonis.com/blog/pgp-encryption)
- [Cyber Skyline Live: PGP Lookup Tutorial](https://www.youtube.com/watch?v=ezH1SrlvkZg&t)
- ChatGPT for initial template
