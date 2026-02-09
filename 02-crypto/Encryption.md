# Encryption

## openssl

OpenSSL can be used to encrypt files using ciphers like CBC, ECB, and OFB. I will be encrypting this image using those three ciphers and then decrypting it with OpenSSL

![linux penguin](tux-96.png)

The process for encryption is very similar across each cipher and follows this basic structure:

`openssl enc <cypher> -in tux-96.png -out tux_cbc.enc -pass pass:yourpassword -pbkdf2`


