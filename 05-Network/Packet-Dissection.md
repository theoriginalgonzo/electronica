Packet dissection is the process of analyzing and breaking down
network packets into their individual protocol layers and 
fields. This allows detailed inspection of the data being
transmitted over a network, revealing information such as
headers, payload, source and destination addresses, and
protocol-specific details. Packet dissection is essential for
network troubleshooting, security analysis, and performance
monitoring, often performed using tools like Wireshark. It 
helps understand how data flows through networks and detect 
anomalies or malicious activity.

For examining IPv4 packets, you will want to refer to the IPv4
header format:

![IPv4 Header Fromat](IPv4Header.png)

| Offsets | 0        | 1        | 2        | 3        |
|---------|----------|----------|----------|----------|
| 0       | 01000101 | 00000000 | 00000000 | 00111100 |
| 4       | 10101001 | 10011010 | 01000000 | 00000000 |
| 8       | 01000000 | 00000110 | 01001111 | 10010011 |
| 12      | 11000000 | 10101000 | 10000000 | 10000000 |
| 16      | 10011111 | 11001011 | 01100000 | 10011010 |


