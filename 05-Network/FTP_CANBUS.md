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
- FTP can be used for both anonymous and authenticated file transfers, and it supports various authentication methods, including username/password and anonymous access.
- FTP is commonly used for uploading and downloading files to and from web servers, as well as for sharing files within a network.

### Common FTP commands 
- `USER`: to identify the username being used for authentication
- `PASS`: to identify the password being used for authentication
- `RETR`: to identify the file being downloaded from the server
- `STOR`: to identify the file being uploaded to the server
- `LIST`: to identify the files and directories being listed on the server
- You can also analyze the data channel to see the actual files being transferred.


### FTP Traffic Gym Guide
    - Using the cloudshark portal, click on packet and select the TCP stream view on the bottom.

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
- CAN BUS is widely used in automotive and industrial applications for communication between various electronic control units (ECUs) in a vehicle or machinery.
- CAN BUS operates on a multi-master, message-oriented protocol, where each device can send and receive messages, but only one device can transmit at a time.
- CAN BUS messages consist of an identifier, data length code, and data payload, and they can be used to control various functions in a vehicle, such as engine performance, braking, and lighting systems.

### CAN BUS Traffic Analysis
- When analyzing CAN BUS traffic, you can look for specific message identifiers to understand the actions being performed by different ECUs.
- You can also analyze the data payload to see the actual information being transmitted, which can help identify potential security issues, such as unauthorized control or data manipulation.
