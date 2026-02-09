# Encryption

## openssl

OpenSSL can be used to encrypt files using ciphers like CBC, ECB, and OFB. I will be encrypting this image using those three ciphers and then decrypting it with OpenSSL

![linux penguin](tux-96.png)

The process for encryption is very similar across each cipher and follows this basic structure:

`openssl enc -<cypher> -in tux-96.png -out tux_<cypher>.enc -pass pass:<yourpassword> -pbkdf2`

This will encrypt our input file into the output file while giving it a password that will be needed for decryption. `-pbkdf2` is a type of key derivation that needs to be specified at the default derivation has been depricated.

The cyphers used in `<cyhper>` were as follows: `-aes-128-cbc -aes-128-ecb -aes-128-ofb` 128 being how many bits long the key is.


