# 🔐 Log Analysis Command Reference Guide
Comprehensive command guide for analyzing SSH, Login, VSFTPD log and custom file format in Linux.

---

# 1. SSH Log Analysis (`auth.log`)

This section covers how to analyze SSH authentication logs to identify login attempts, usernames, timestamps, and successful logins.

---

## Question 1: 

```
cat auth.log | head
```

- From this you will get answer myraptor.

## Question 2: 

```
 cat auth.log | head
```

- In this result you will look for key words like failed password , accepted password etc and this is for sorted data if it is not sorted use

```
 cat auth.log | head | sort
```

- From this you will get answer 169.139.243.218

## Question 3,4:

```
 cat auth.log | grep password
```

- This shows all failed and accepted password attempts.

- If timestamps are not sorted use:

```
cat auth.log | grep password | sort
```
From this you will identify the second and third failed password attemptfrom ip address.

## Question 5:
```
cat auth.log | grep password
```

- In the output you will see multiple attempts for username Harvey.

- From this you will get answer Harvey.

## Question 6:
```
cat auth.log | grep "Accepted password"
```
- This filters successful SSH logins.

- From this you will get the IP address that successfully logged in.


# 2 Login Log Analysis (login.log)

- This section analyzes login attempts, usernames, and IP addresses.

---

## Question 1:

```
cat login.log | wc -l
```

- This counts total login attempts (total lines in file).


## Question 2:

```
cat login.log | awk '{print $4}' | sort | uniq | wc -l
```

- This gives total number of unique users.

## Question 3,4:

```
cat login.log | awk '{print $4}' | sort | uniq -c | sort -n
```

- This shows login attempt count per user.

- From this you can identify the user with the most attempts.

## Question 5:

```
cat login.log | awk '{print $1}' | sort | uniq -c | sort -n
```

- This shows login attempts per IP address.

- From this you can identify the most active IP.

## Question 6:

```
cat login.log | awk '{print $3,$4}' | sort | uniq | awk '{print $2}' | sort | uniq -c | sort -n
```

- This shows unique user and IP combinations.

- From this you can determine which user logged in from the most unique IP addresses.

# VSFTPD Log Analysis (vsftpd.log)

- This section analyzes FTP login activity, uploads, downloads, and suspicious behavior.

---

## Question 1 : 
```
cat vsftpd.log | grep "ftpuser" | head
```
- This gives the IP address of ftpuser

## Question 2: 

```
cat vsftpd.log | grep -i mkdir | head -1
```

- This shows the first directory created in last column as path 

## Question 3:

```
cat vsftpd.log | grep "ftpuser" | grep -i mkdir | tail -1
```

- This shows the last directory created by ftpuser.

## Question 4:

```
cat vsftpd.log | grep "ftpuser" | grep "OK UPLOAD" | awk -F ',' '{print $2}' | awk -F '.' '{print $NF}' | sort | uniq -c | sort -n
```

- This counts uploaded file extensions by ftpuser.
- From this you identify the most uploaded file type.

## Question 5,6:

```
cat vsftpd.log | grep -v "ftpuser"
```

- this will grep something which is not ftpuser
- From this you can analyze other users or suspicious activity.

## Question 7:

```
cat vsftpd.log | grep -v "ftpuser" | grep "OK UPLOAD" | cut -d ',' -f3 | awk '{sum += $1} END {print sum}'
```
- This calculates total upload size by users other than ftpuser.

## Question 8:

```
cat vsftpd.log | grep "ftpuser" | grep "OK UPLOAD" | cut -d ',' -f3 | awk '{sum += $1} END {print sum}'
```

- This calculates total upload size by ftpuser.

## Question 9:

```
cat vsftpd.log | grep "ftpuser" | grep "OK DOWNLOAD" | cut -d ',' -f3 | awk '{sum += $1} END {print sum}'
```
- This calculates total download size by ftpuser.

## Question 10:

```
cat vsftpd.log | grep -i "login"
``` 

- This gives list of login attempts.

- If ftpuser normally logs in from 10.0.0.123 but you see login from 10.3.0.6, then 10.3.0.6 is suspicious.



# Custom File Format 

---

- When You run the give python program and transfer output in different file you will get most of the answer at the header and footer.
- In python program, custom file is named as hard.sky so before you run python program make sure of this.
- readable_sky.txt in this file i have my output of my python program.

## Question 2:

```
echo "U0tZLVBBUlMtNzMyNQ==" | base64 -d
```

- you will get the flag.

## Question 6:

```
awk '{print $1; print $3}' readable_sky.txt | sort | uniq | wc -l
```

## Question 7,8:

```
grep '-' readable_sky.txt | awk '{print $2, $(NF-1)}' | sort | awk '{sum[$1] += $2} END {for (ip in sum) print ip, sum[ip]}' | sort -k2 -nr | head -1
```

## Question 9:

```
 cat readable_sky.txt | awk '{print $6,$9}' | sort |  awk '{sum[$1] += $2} END {for (ip in sum) print ip, sum[ip]}' | sort -k2 -nr | head -1
```
