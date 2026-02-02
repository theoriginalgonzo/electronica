# OSI topics

---

Images and data:

- Meta
  - Image metadata
- Barcode
  - Familiarize and document
- add QR codes
- AIM hackathon resources: 
  - https://github.com/wrightedu/Make-IT-Wright-2023
  - https://github.com/wrightedu/Make-IT-Wright-2023/wiki

---

Network and DNS

- Lookup
  - DNS and authorship
- DNS
  - The system that makes domain names into ip addresses
- Authorship
  - Who can access, publish or sign DNS data/records
- Questions
  - 1. What type of DNS record holds the DNSSEC public signing key?
  - The DNSSEC (domain name ssystem security extensions) adds security and uses public/private keys. That public key is stored in the DNSKEY record
  2. What type of DNS record is used to map hostnames to IPv6 addresses?
  - The type of DNS record that is used to map hostnames to IPv6 addresses is AAAA (ex:2606:2800:220:1:248:1893:25c8:1946)
  3. What type of DNS record is used to delegate a DNS zone?
  - To delegate a DNS zone just assigns a domain to a server
  - The server that does this is called NS 

- WHOIS
  - more DNS, ICANN
- more DNS
  - WHOIS provides data about DNS names like who registered the domain and when someone registered the domain 
- ICANN
 - Global organization that oversees the DNS to make sure its stable and safe
- Questions 
  1. Who is the registrar of this domain?
  - Go to the ICANN lookup results and search cityinthe.cloud
  - Look for the registar information and on that info it says Dynadot, LLC
  2. On what day was this domain first registered?
  - On created field and it says 2-16-2016
  3. What is this domain's registry domain ID?
  - D15CD1AC4DEB54207A5048A69B9FC0558-ARI under registry domain ID
  4. What is the Top-Level Domain (TLD) of this domain?
  - The TLD is the rightmostlabel of the domain name so it would be .cloud 
  5. What organization manages the TLD used by cityinthe.cloud?
  - Looked up .cloud TLD and found that its managed by Aruba S.p.A.
---

NIST

- Threat Intel
  - CVEs
  - [CPE lookup](https://nvd.nist.gov/products/cpe/search)

---
## Web

- HTTP Headers
  - URL 
    - A type of URI that specify the location of resources and how to access it.
  - URI
    - General identifier for resources that identify resources by name and location or both. ALL URLs are URIs but not all URIs are URLs.
  - Protocols
    - Protocols are set of rules that define how data sent and received 
    - HTTP for transfer web page
    - HTTPS for secure HTTP
    - FTP for file transfer
    - SMTP for sending mail
    - DNS for Domain name resolution

  - add GET, POST, and FTP equivalents
    - GET 
        - used to request data, parameters in URL, doesn't change server state
    - POST
        - used to send data, data in request body, can change server state
    - FTP
        - FTP used for upload and download files
        - used control channel and data channel


- To solve In Linux, HTTP request headers can be viewed using curl command with the verbose option. Running curl -v <URL> displays the outgoing HTTP request, where lines prefixed with > show request headers such as Host, User-Agent, and Accept.


- To solve the question about headers you have to pick up keywords from the question and search those keywords on this site with ctrl + F [Wikipedia page](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields) It takes time to find right http header.


- SSL
  - SSL certificate chains
    - SSL certificate chains establish trust by linking a website’s certificate to a trusted root Certificate Authority through one or more intermediate CAs(certificate authorities).
  - add CSA and trust

    - A Certificate Authority (CA) is a trusted third party that:

        - Issues SSL certificates

        - Verifies website identities

        - Signs certificates cryptographically

    - Trust in SSL means:

        - Your browser already trusts certain root CAs

        - These trusted root certificates are preinstalled in the OS/browser

        - If a website’s certificate chains up to one of these roots → it is trusted

        - If it does not → warning 

- To solve in linux, SSL certificates can be viewed using curl command with curl -vI <URL> where you can look for SSL connection using TLS and server certificate. If server certificate is self signed then it is untrusted.

- To solve the question from this section you have to go to site information you can access that from clicking left side of icon(== something like that) in url bar. From there you have to click "connection secure" and after that you have to click "certificate is valid". Now you can see the details like issued to or issued by in genral tab. if you go to details you can certificate heirachy and other details.

---

## GPG/PGP Lookup

- Kijowski

