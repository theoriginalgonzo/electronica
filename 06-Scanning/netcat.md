# Netcat (nc) Beginner Guide

Netcat is often called the **“Swiss Army knife of networking”**.  
It can open TCP/UDP connections, listen on ports, transfer files, scan ports, and create shells.

---

# 1. Basic Syntax

` nc [options] host port `

- Example : `nc example.com 80`


Connects to port **80** on example.com.

---

# 2. Most Important Netcat Flags

| Flag | Meaning |
|-----|--------|
| -l | Listen mode (wait for connection) |
| -p | Specify port |
| -v | Verbose output |
| -vv | More verbose |
| -n | No DNS lookup |
| -u | UDP mode |
| -z | Scan mode (no data transfer) |
| -w | Timeout |
| -e | Execute program after connect |
| -k | Keep listening after connection closes |
| -c | Execute command via shell |
| -4 | Force IPv4 |
| -6 | Force IPv6 |

---

# 3. Connect to a Server

- `nc 192.168.1.10 80` or `nc google.com 80`

- 
You can manually type HTTP requests now and you will get response.


---

# 4. Listen for a Connection

`nc -lvnp 4444`


Explanation:

- `-l` listen
- `-v` verbose
- `-n` no DNS lookup
- `-p` port

---

# 5. Chat Between Two Machines

Machine 1 (listener)
`nc -lvp 4444`


Machine 2 (connect)
`nc 192.168.1.5 4444`

Now both machines can chat.


---

# 6. When to Use Netcat vs Other Tools

| Tool | Use |
|----|----|
| Netcat | Simple connections |
| Gobuster | Directory brute forcing |
| Nmap | Port scanning |
| Curl | HTTP requests |

---
