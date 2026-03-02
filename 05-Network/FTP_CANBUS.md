# Network Traffic Analysis

## 0. Outline
- [1. Network Traffic Analysis](#1-Network-Traffic-Analysis)
- [2. FTP](#2-FTP)
- [3. CAN BUS](#3-CAN-BUS)
- [4. Citations](#4-Citations)

## 1. Network Traffic Analysis
- Network traffic analysis is the process of intercepting, recording, and analyzing network traffic to understand the behavior of a network, identify potential security threats, and troubleshoot network issues.
- Tools commonly used for network traffic analysis include Wireshark, tshark, tcpdump, cloudshark.
- Network traffic analysis can be used to identify malicious activity, such as unauthorized access, data exfiltration, and malware communication.

## 2. FTP
- FTP (File Transfer Protocol) is a standard network protocol used for transferring files between a client and a server over a TCP/IP network.
- FTP operates on two separate channels: the control channel for sending commands and receiving responses, and the data channel for transferring files.
- FTP can be used for both anonymous and authenticated file transfers, and is commonly used for uploading and downloading files to and from web servers, as well as for sharing files within a network.
### Common FTP commands 
- `USER`: to identify the username being used for authentication
- `PASS`: to identify the password being used for authentication
- `RETR`: to identify the file being downloaded from the server
- `STOR`: to identify the file being uploaded to the server
- `LIST`: to identify the files and directories being listed on the server
- You can also analyze the data channel to see the actual files being transferred.


### FTP Traffic Gym Guide
    Using the cloudshark portal, click on packet and select the TCP stream view on the bottom.

1. What was the first username:password combination attempt made to log in to the server? ex. 'user:password'
2. What software is the FTP server running? (Name and version)
3. What is the first username:password combination that allows for successful authentication?
4. What is the first command the user executes on the ftp server?
    - Follow the TCP streams to find the first command executed after successful authentication.
5. What file is deleted from the ftp server?
6. What file is uploaded to the ftp server?
    - You can also use filter `ftp.response.code == 230` for successfully authenticated sessions (code 230).
7. What is the filesize (in bytes) of the uploaded file?
    - Find a LIST command after the upload and check the file size in the response (double click on the response to see the details).
8. What file does the anonymous user download?

## 3. CAN BUS
- CAN BUS (Controller Area Network) is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other without a host computer.
- CAN BUS operates on a multi-master, message-oriented protocol, where each device can send and receive messages, but only one device can transmit at a time.
- CAN BUS messages consist of an identifier, data length code, and data payload, and they can be used to control various functions in a vehicle, such as engine performance, braking, and lighting systems.

### CAN BUS Traffic Gym Guide
    Install Wireshark and open the provided CAN bus capture file. Click on a packet and in details under CAN ID, double click the `= ID` field and select "Apply as Column". Do the same for first field uner Data, and select "Apply as Column". You should now have two new columns in the packet list view, one for CAN ID and one for Data. Export the packet disection as a CSV file and use it to answer the questions.

1. How many unique CAN Bus IDs are present in this capture?
    - Use `awk -F ','` to print IDs and then find number of unique IDs using `sort`, `uniq`, `wc -l` commands.
2. How many speed update messages are present in this capture?
    - Code snippet has `int speed_id = 589;` which indicates that speed updates are sent with CAN ID 589. Use `grep` to find number of messages with this ID.

3. What is the maximum speed, in mph, that this vehicle reached in the capture? 
    - Extract the data field for messages with CAN ID 589, `awk -F ',' '$7 ~ /589/ {print $8}'`, into a new file. Then, use the `python3 max_speed.py data.txt` script to find the maximum speed in mph. (`tr -d '"'` can be used to remove quotes from the data field if needed).

