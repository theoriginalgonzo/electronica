# DNS 

### Question 1:

```
tshark -r DNS.pcap -Y dns -T fields -e dns.qry.type 
```

- here -r DNS.pcap says read packets from this file. -Y dns specify the protocal type. -T fields says only output some specific part of packet and -e  dns.qry.type says Extract the field DNS Query Type from each packet.

- with this you will get 252 as output and you search on google what is 252 dns query type refers it will say 'AXFR'


### Question 2:

```
tshark -r DNS.pcap -Y dns -T fields -e dns.qry.name
```

- This will give answer etas.com

### Question 3:

```
tshark -r DNS.pcap -Y "dns.flags.response == 1" -T fields -e dns.count.answers
```

- dns.flags.response == 1 -> show DNS responses and dns.count.answers → prints number of answer records

- This will give answer of 4.

### Question 4:

```
tshark -r DNS.pcap -Y "dns.flags.response == 1" -T fields -e dns.resp.ttl
```

- dns.flags.response == 1 → only DNS responses and dns.resp.ttl → prints TTL values

- Answer would be 3600.

### Question 5:

```
 tshark -r DNS.pcap -V | grep welcome
```

- answer should be welcome.etas.com


# Pandora

### Question 1,2,3:                                                 

```
tshark -r pandora.pcap -Y "tcp.port != 22 && tcp.port != 80"
```                                 

- After You run this you will see the conversion where client intialize it so you will get client ip : 10.1.0.217 and server ip : 10.1.0.20 and server port 60123. 

### Question 4,5,8:

```
tshark -r pandora.pcap -Y "tcp.port == 60123" -T fields -e data
```

- This command extracts only the data from the packets and you will find 0417 as magic byte which is 1047 in decimal. above magic byte you will see 05 which is answer of question 5.

-  After that you will see 0xa0 which is used for answer question number 8. The hash-length can be determined by taking the total number of requests (5) and dividing it by the length of the response as advertised by the server 0xa0 or 160 decimal, yielding a result of 32 bytes.

### Question 6,7:

```
tshark -r pandora.pcap -V -Y "tcp.port == 60123 && data contains 04:17"
```

- this will give me packets on pory 60123 which has magic byte in as data so when you check 5545 Frame in data starts from 00 00 00 58 which is the size of first request in bytes it is 88. and you check for second request you can look for 04 17 magic byte first and then 00 00 00 48 which size of second request in bytes 72. 

### Question 9,10:
```
tshark -r pandora.pcap -Y "tcp.port == 60123" -T fields -e data
```

- The 5 block of hash is answer of question 9 and for question 10 you have to use only first 32 bytes of 6 th block of hash.


### Question 11:

```
 tshark -r pandora.pcap -Y "tcp.port == 60123 && data" -T fields -e data | xxd -r -p | base64 -d -i | strings
```

- Answer is :  NCL-FJCG-1632

- tshark -r pandora.pcap reads pcap file, -Y  "tcp.port == 60123 && data" filters file for only tcp port 60123 and if packet has data in it.

-  -T fields -e data extract payload field
-  xxd -r -p convert hex to binary
-  base64 -d -i decode base64
- strings print only readable text

