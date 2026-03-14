# Decrypting HTTPS Traffic Using Wireshark

## Introduction

### HTTPS traffic is normally encrypted using the Transport Layer Security, which replaced the older Secure Sockets Layer.

Encryption prevents attackers from reading transmitted data such as passwords, cookies, or session tokens. However, if the TLS session keys are available, network analysis tools can decrypt the traffic.

In this gym, we use Wireshark together with an SSL key log file (sslkeylog.log) to decrypt the captured HTTPS traffic stored in the provided SSL Decrypt.pcapng file.

## Required Files

The challenge provides two files:

SSL Decrypt.pcapng – the packet capture containing encrypted HTTPS traffic

sslkeylog.log – a log file containing TLS session secrets used to decrypt the traffic

### Step 1 – Open the Packet Capture

Launch Wireshark.

Click File → Open.

Select the file SSL Decrypt.pcapng.

You will see many packets, most of which appear as TLS encrypted traffic.

### Step 2 – Configure the TLS Key Log

To allow Wireshark to decrypt the traffic, we must load the provided TLS key log.

In Wireshark, open Edit → Preferences.

In the left panel, expand Protocols.

Scroll down and select TLS (or SSL in older Wireshark versions).

Locate the field labeled:

(Pre)-Master-Secret log filename

Click Browse.

Select the file sslkeylog.log.

Click OK.

Wireshark will now automatically use the session keys in this file to decrypt the TLS traffic.

### Step 3 – Verify Decryption Worked

After loading the key log file:

Previously encrypted TLS packets will now show decrypted application data.

Some packets will now display HTTP instead of TLS.

This indicates the TLS session has been successfully decrypted.

### Step 4 – View the Decrypted Traffic

To read the decrypted content:

Right-click any packet that contains TLS or HTTP data.

Select:

Follow → TLS Stream

Wireshark will reconstruct the communication between the client and server.

You will now see the plaintext HTTP request and response data, which may include:

URLs

Form submissions

Cookies

Hidden flags or messages

Question 1: What Cipher Suite was chosen by the secure socket server?
Select packet #6 (the TLS Server Hello) and look for the “Cipher Suite”. 
This can be found in the packet dissection under Transport Layer Security → TLSv1.2 Record Layer: Handshake Protocol: Server Hello → Handshake Protocol: Server Hello → Cipher Suite

Answer to question 1:  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256


Question 2: What is the domain covered by the SSL key?

Select packet #6 (the TLS Server Hello) and look for the “common name” of the SSL certificate. This can be found in the packet dissection under Transport Layer Security → TLSv1.2 Record Layer: Handshake Protocol: Certificate → Handshake Protocol: Certificate → Certificates → Certificate.

Next, look under signed certificate then under issuer where you will see an email address with the domain we are looking for.

Answer to question 2: tomsvacations.com 

### Step 5 – Locate the Hidden Flag

Scroll through the TLS stream window and look for readable text.

Often the flag will appear inside:

HTTP responses

HTML page content

JSON data

API responses

Question 3: What is the flag transferred over HTTPS?

Follow the TLS stream for packet #10 (the request for /flag.txt)

Answer to question 3: SKY-LADN-1435



