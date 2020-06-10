"""
! Fixed XOR
* Write a function that takes two equal-length buffers and produces their XOR combination.

* If your function works properly, then when you feed it the string:
* 1c0111001f010100061a024b53535009181c

* ... after hex decoding, and when XOR'd against:
* 686974207468652062756c6c277320657965

* ... should produce:
* 746865206b696420646f6e277420706c6179
"""
import string

def fixed_xor(hex_input_1, hex_input_2):
    '''
    Takes 2 hex strings of the same length, and returns the "XOR" of the two strings
    '''
    assert all(ch in string.hexdigits for ch in hex_input_1) == True, "Input 1 is not a valid hex string!"
    assert all(ch in string.hexdigits for ch in hex_input_2) == True, "Input 2 is not a valid hex string!"
    assert len(hex_input_1) == len(hex_input_2), "Inputs are not of the same length"

    return hex(int(hex_input_1, 16) ^ int(hex_input_2, 16))[2:]

testcases = {
    "1c0111001f010100061a024b53535009181c 686974207468652062756c6c277320657965":"746865206b696420646f6e277420706c6179",
    "075bcd15 3ade68b1":"3d85a5a4"
}
def main():
    for i, o in testcases.items():
        inputs = i.split(" ")
        assert fixed_xor(inputs[0], inputs[1]) == o

if __name__ == "__main__":
    main()