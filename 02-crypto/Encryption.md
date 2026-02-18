# Encryption

## openssl

OpenSSL can be used to encrypt files using ciphers like CBC, ECB, and OFB. I will be encrypting this image using those three ciphers and then decrypting it with OpenSSL

![linux penguin](tux-96.png)

The process for encryption is very similar across each cipher and follows this basic structure:

`openssl enc -<cypher> -in tux-96.png -out tux_<cypher>.enc -pass pass:<yourpassword> -pbkdf2`

This will encrypt our input file into the output file while giving it a password that will be needed for decryption. `-pbkdf2` is a type of key derivation that needs to be specified at the default derivation has been depricated.

The cyphers used in `<cyhper>` were as follows: `-aes-128-cbc -aes-128-ecb -aes-128-ofb` 128 being how many bits long the key is.

To decrypt the images we take the same command structure used for the encryption but change the input file and add the `-d` flag:

`openssl enc -<cypher> -d -in tux_<cypher>.enc -out tux_decrypted_<cypher>.png -pass pass:<yourpassword> -pbkdf2`

## RSA

I am now going to decrypt a message that has been encrypted with RSA. The basic steps of RSA encryption are:

### Generate the key pair

1. Make two prime numbers (p and q)

2. Calculate p\*q (n) 

3. Calculate d and e so that d\*e ≡ 1mod(p-1)(q-1). Which means that when you multiply d and e the remainder when divided by (p-1)(q-1) is 1.

4. The public key is n and e while the private key is d p and q

### Encrypt the message

5. Convert the plaintext to an integer (m).

6. Obtain the cyphertext (c) where c ≡ m^e^

### Decrypt the message

7. Calculate the plaintext where m ≡ c^d^

I already have the values of n e and c. Those being:

```
n = 1079
e = 43
c = 996 894 379 631 894 82 379 852 631 677 677 194 893
```

We know that n=p\*q so by factoring 1079 we get the only two factors 83 and 13, so p=83 and q=13, and by substituting these values into the equation in step 3 we can calculate that d=595.

So now we have all the information we need in:

```
n = 1079
e = 43
c = 996 894 379 631 894 82 379 852 631 677 677 194 893

p = 83
q = 13
d = 595
```

Finally to decypher the message we use the decryption equation of m=c^d^ (mod n) for every value of c, converting the result into a ASCII character. So for the first value, m = 996^595^ mod1079 = 83, which in ASCII is "S"


I made a python script to calculate each plaintext character:

```
c = <I just typed each c value in>
d = 595
n = 1079

result = pow(c, d, n)

print(f"{c}^{d} mod {n} = {result}")
```

After running this script for each c value I got the final message:
`SKY KRYG 5530`

(you could also just use the [tausquared](https://www.tausquared.net/pages/ctf/rsa.html) rsa calculator but I made the script before I saw that was a thing.)

## Thunderbird

By downloading [Thunderbird](https://www.thunderbird.net/en-US/) you can use GPG keys to encrypt your emails. By uploading your public GPG key to Thunderbird you can send emails that can only be read by someone that has that public key's corresponding private key.
