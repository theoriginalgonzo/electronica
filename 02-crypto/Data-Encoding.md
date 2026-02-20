# NCL Steganography Challenge – Hidden Flag with `strings`

## Overview
This challenge provides hands-on experience with basic Linux tools to uncover hidden messages using **steganography**.

An image file was modified to embed a hidden flag within its raw binary data. The goal of the challenge is to extract that hidden flag using command-line tools.

---

## Challenge Objective
**Question:**  
What is the hidden flag in the image?

**Hint provided:**  
The hidden flag can be found using the Linux `strings` program.

---

## Key Concepts

### Binary vs Text Data
Files such as images contain:
- **Printable characters** (letters, numbers, symbols)
- **Non-printable binary data**

Not all binary values correspond to readable characters.  
The `strings` command extracts only the **readable text** from a binary file.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| `strings` | Extracts readable text from binary files |
| `grep` | Searches for specific patterns in text output |

---

## Solution Walkthrough

### Step 1: Extract readable strings from the image
Run the following command:

```
strings -n 5 Steg1.jpg | grep -E '^[A-Za-z0-9_-]{5,}$'
```
- grep uses Regex expression to elimate all other charcters beside a - z, A - Z, 0 - 9, - and _
- strings output random charcters so -n 5 is used for readable characters 
- this way we get short output of strings and we can find Flags very easily.
