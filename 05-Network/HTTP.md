# HTTP
## 1. What Linux tool was used to execute a file download?
- Download Wireshark
- Open the pcap file 
- Apply http.request
- Click on the result 
- Expand Hypertext transfer protocol and look for user-agent
- Answer is wget
## 2. What is the name of the web server software that handled the request?
- Now apply http.response
- Click on the result 
- Under Hypertext transfer protocol look for server
- Answer is nginx
## 3. What IP address initiated the request?
- Stay on http.response
- expand internet protocol version 4
- Look for destination address
- the answer is 192.168.1.140
## 4. What is the IP address of the server?
- Stay on http.response
- under internet protocol version 4
- Look for source address
- the answer is 174.143.213.184
## 5. What is the MD5 sum of the file downloaded?
- Open the file 
- File -> export objects -> HTTP
- Click the file and save it
- Open a terminal and run md5sum "filename" 
- Answer is 966007c476e0c200fba8b28b250a6379 