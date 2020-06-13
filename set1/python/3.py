"""
! Single-byte XOR cipher

* The hex encoded string:
* 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
* ... has been XOR'd against a single character. Find the key, decrypt the message.

* You can do this by hand. But don't: write code to do it for you.
? How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

* Achievement Unlocked
* You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

* This solution uses a pretty primitive scoring mechanism 
* Character frequencies taken from https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
"""
from utils import score

def decode(ciphertext, key):
    k = ''.join([chr(b ^ key) for b in bytearray.fromhex(ciphertext)])
    return k

def single_byte_xor_cipher(hex_input):
    return max(range(256), key = lambda x: score(decode(hex_input, x)))

def main():
    ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    key = single_byte_xor_cipher(ciphertext)
    print(decode(ciphertext, key))

if __name__ == '__main__':
    main()
