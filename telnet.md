# Telnet

In this gym, we'll take a look at some telnet traffic with wireshark.  Telnet is sent unencrypted so there is no need to feed in an encryption key like past exercises.  

First, open the Telnet.pcap file in wireshark.  Then find the first Telnet packet, which, in this case, is packet 4.  Highlight it then right click it and select, follow TCP stream.  

Once, you've selected Follow TCP stream, at the bottom you'll see the drop down box that says "Show as" open it and select the very first option, ASCII.

After you select show as ASCII, you will see the answer to all questions.

Login and password are displayed line by line like this:

t
t
e
e
s
s
t
t

It is listed line by line like this due to how line endings are handled.

Also, each character is displayed twice because the local terminal echoes your input and so does the telnet server.

### Questions 1:
What is the username that was used to log in?

### Answer to question 1: 
test

### Question 2:
What is the password that was used to log in?

### Answer to question 2: 
capture

### Question 3:
What command was executed once the user was authenticated?

### Answer to question 3: 
uname -a

The uname -i command is used on Linux systems to display the system’s hardware platform (machine architecture).

Right after the uname -i command is executed you can see this output:

Linux cm4116 2.6.30.2-uc0 #3 Tue Feb 22 00:57:18 EST 2011 armv4tl unknown

This shows the hostname right after linux and also the date it was captured and lastly, it shows the CPU architecture.

### Question 4:
In what year was this capture created?

### Answer to question 4: 
2011

### Question 5:
What is the hostname of the machine that was logged in to?

### Answer to question 5: 
cm 4116

### Question 6:
What CPU architecture does the remote machine use?

### Answer to questoin 6: 
armv4tl


