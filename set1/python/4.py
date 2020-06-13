"""
! Detect single-character XOR
* One of the 60-character strings in this file has been encrypted by single-character XOR.
* Find it.
* (Your code from #3 should help.)
"""

from utils import score, decode

def main():
    with open('4.txt', 'r') as f:
        ip = f.read().split()
        keys = [max(range(256), key = lambda k: score(decode(i, k))) for i in ip]
        print(
            max(
                [
                    {
                        "ciphertext": ip[i],
                        "key": keys[i],
                        "decoded": decode(ip[i], keys[i])
                    } 
                for i in range(len(keys))
                ],
                key = lambda k: score(k["decoded"])
            )
        )

if __name__ == "__main__":
    main()
