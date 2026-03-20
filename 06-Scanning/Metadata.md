# Scanning & Reconnaissance

## Metadata Gym
The Instance Metadata Service (IMDS) allows instances to access information about themselves. This metadata includes details such as network configuration, associated events, the attached IAM role, and more. To access the service and retrieve the metadata, you make HTTP requests to various endpoints. 

### Metadata Gym Guide
    - Use `curl` to make HTTP requests to the metadata service endpoints. The base URL for the metadata service is http://metadata.services.cityinthe.cloud:1338/. You can append different returned endpoints to this base URL i.e `/latest/meta-data`, etc.

1. What availability zone is this instance hosted in?
    - Follow the `.../placement/availability-zone` endpoint

2. What is the security credentials role named?
    - Find the `.../iam/security-credentials` endpoint

3. What is the instance type being used?
    - Find the `.../instance-type` endpoint

4.  What is the operating system name and version number?
    - Use the returned AMI ID from the `.../ami-id` endpoint to find the OS name and version number using https://cloud-images.ubuntu.com/locator/ec2/.

5. What is the flag?
    - The flag can be found at the endpoint `.../network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv4-cidr-blocks` To find it, you would need to follow all the meta-data endpoints. Or you can use the crawl.py script to crawl through the metadata endpoints and then look for the flag.  You can run the script using `python3 crawl.py http://metadata.services.cityinthe.cloud:1338/latest/meta-data`.