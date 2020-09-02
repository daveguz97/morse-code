#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'David Guzman with help from Bethsheba'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits = bits.strip('0')
    frequency = min([len(bit)
                     for bit in bits.split('1') + bits.split('0') if bit])
    decoder = bits.replace(
        '111' * frequency, '-').replace(
            '1' * frequency, '.').replace(
                '0000000' * frequency, '   ').replace(
                    '000' * frequency, ' ').replace(
                        '0' * frequency, ''
    )

    print(decoder)
    return decoder


def decode_morse(morse):
    decipher = ''
    double_spaces = '  '
    morse = morse.split(double_spaces)
    for word in morse:
        word = word.split()
        for letter in word:
            decipher += MORSE_2_ASCII[letter]
        decipher += " "
    morse_string = decipher.strip()
    return morse_string


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
