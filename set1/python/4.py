from utils import score

def decode(ciphertext, key):
    k = ''.join([chr(b ^ key) for b in bytearray.fromhex(ciphertext)])
    return k

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