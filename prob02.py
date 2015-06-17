#!/usr/bin/python

from prob01 import hex_to_byte_array


def hex_xor(s1, s2):
    b1 = hex_to_byte_array(s1)
    b2 = hex_to_byte_array(s2)
    xor = bytearray()
    for i in range(len(b1)):
        xor.append(b1[i] ^ b2[i])
    return bytes(xor).encode('hex')


if __name__ == '__main__':
    print hex_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')

