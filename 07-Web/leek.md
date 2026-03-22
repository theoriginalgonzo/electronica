# Web Application Exploitation 

## 0. Outline
- [1. Buffer Vulnerabilities](#1-Buffer-Vulnerabilities)
- [2. Find the Leek](#2-Find-the-Leek)
- [3. Exploitation](#3-Exploitation)
- [4. Citations](#4-Citations)

## 1. Buffer Vulnerabilities
- Older Node.js versions have vulnerabilities involving the Buffer constructor. When the Buffer() constructor is passed a number rather than a string, it allocates a new buffer of that specified size. However, the contents of this buffer are not initialized and may contain sensitive data from previous allocations. 
- If sensitive information like a flag or secret key was recently handled by the server, it may still reside in that uninitialized memory.

## 2. Find the Leek
- To find the leak, look at network communication using Developer Tools (F12).
- Observe Requests: Adding an item to the list (e.g., "Banana") reveals a JSON payload: `{"content": "Banana"}`.
- Analyze Responses: In the "Preview" or "Response" tab, note if the server returns data as a Buffer object (e.g., `{"type": "Buffer", "data": [98, 97, 110, ... ]}`).

## 3. Exploitation
- Once you suspect the server is using an unsafe Buffer constructor, you can attempt to "leak" memory by changing the data type of your input. 
- Instead of sending a string, send a number (e.g., `{"content": 100}`) to trigger the allocation of a new buffer. This instructs the server to allocate a buffer of that size using whatever is currently in its memory.
- The server may respond with a Buffer containing uninitialized memory, which could include sensitive information such as the flag.
- Use the following `curl` command to send a request with a numeric payload:
```
curl 'https://0c34ea85d35b6f1ca5cee5ef65b02e23-leek.web.cityinthe.cloud/add' \
    -H 'Content-Type: application/json' \
    --data-raw '{"content": 100}'
```

## 4. Citations
- [Leek Challenge](https://trove.cyberskyline.com/367e2642f46442a09912be18cb882eba)
- Gemini for Buffer vulnerability explanation and exploitation steps.
- Copilot for overall outline and structure.