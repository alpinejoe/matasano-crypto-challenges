#!/usr/bin/python

from prob01 import hex_to_byte_array


def compare_etaoin_frequency(x, y):
    etaoin = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    global frequency
    ret = frequency[x] - frequency[y]
    if ret == 0:
        return etaoin.find(y) - etaoin.find(x)
    return ret


def get_etaoin_score(b, i):
    # https://inventwithpython.com/hacking/chapter20.html
    # Get list of letters, ordered by the frequency of occurrence
    score = 0
    global frequency
    frequency = {}
    for j in range(ord('A'), ord('Z') + 1):
        frequency[chr(j)] = 0
    for j in b:
        c = chr(i ^ j)
        if not c.isalpha():
            continue
        c = c.upper()
        frequency[c] += 1
        score += 1  # String with no letters will score full otherwise

    # We should be sorting by ETAOIN for letters having the same frequency
    frequent_letters = sorted(frequency, cmp=compare_etaoin_frequency, reverse=True)

    # Score based on probability of letter being in the given phrase
    # http://www.rinkworks.com/words/letterfreq.shtml
    # Score based on only high frequency letters won't work, it only accounts for a partial spectrum
    high_frequency = frequent_letters[:6]
    low_frequency = frequent_letters[-6:]
    for j in 'ETAOIN':
        if j in high_frequency:
            score += 1
    for j in 'VKJXQZ':
        if j in low_frequency:
            score += 1

    return score


def single_byte_xor_cipher(s):
    b = hex_to_byte_array(s)
    max_score = 0
    cipher = 0

    for i in range(127):
        score = get_etaoin_score(b, i)
        if score > max_score:
            max_score = score
            cipher = i

    original = bytearray()
    for j in b:
        original.append(cipher ^ j)
    print 'Original message: ' + bytes(original)

    return cipher


if __name__ == '__main__':
    print single_byte_xor_cipher('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
