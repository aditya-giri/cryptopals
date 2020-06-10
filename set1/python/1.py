"""
! Convert hex to base64
* The string:
* 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

* Should produce:
* SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

* So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

! Cryptopals Rule
! Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""

from base64 import b64encode

def hex_to_base64(hex_string):
    return b64encode(bytes.fromhex(hex_string)).decode()

def main():
    # Test the hex_to_base64 function
    hex_inputs = ["49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d", "546573742048455820496e707574"]
    b64_outputs = ["SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t", "VGVzdCBIRVggSW5wdXQ="]
    
    for i in range(len(hex_inputs)):
        assert hex_to_base64(hex_inputs[i]) == b64_outputs[i]

if __name__ == '__main__':
    main()