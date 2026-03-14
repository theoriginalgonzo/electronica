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

### Step 5 – Locate the Hidden Flag

Scroll through the TLS stream window and look for readable text.

Often the flag will appear inside:

HTTP responses

HTML page content

JSON data

API responses

Once found, record the flag as the solution to the challenge.





