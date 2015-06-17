#!/usr/bin/python

def encrypt_repeating_xor(s, key):
    b = bytearray(s)
    key = bytearray(key)
    i = 0
    for c in range(len(b)):
        b[c] = b[c] ^ key[i % len(key)]
        i += 1
    return bytes(b).encode('hex')


if __name__ == '__main__':
    input = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    print encrypt_repeating_xor(input, 'ICE')
