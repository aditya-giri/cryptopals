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

def score(word):
    letter_score = {
        'E' : 12.0,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07,
        ' ' : 12.0,
    }
    score = 0
    for ch in word:
        if ch.upper() in letter_score.keys():
            score += letter_score[ch.upper()]*100
    return score

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
