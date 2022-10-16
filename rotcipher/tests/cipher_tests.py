from typing import List

import unittest

from ..lib import apply_cipher, reverse_cipher


class CipherTests(unittest.TestCase):

    _ORIGINAL_VALUE = 'This is a test of the cipher functions.'
    _CHARACTER_OPTIONS = ['C', '4', 'Q', ']', 'v', 'z', 'O', 'T', ',', 'y', 'R', 'j', ' ', 'd', '0', 'g', '}', 'i',
                          '7', 'X', '<', '"', '8', '3', 'B', '+', "'", 'K', 'L', 'J', 'Y', 'h', '1', '@', '/', 'U',
                          'I', 'u', '{', '?', '*', 'k', '^', 'N', 'S', ':', '-', 'G', 'V', 'H', '%', 'm', 'r', 'W',
                          'q', 'l', '[', 'F', '|', '!', 'E', '$', 'f', 'x', 'P', ')', '.', 'c', '`', '(', '6', '&',
                          's', '~', '5', 'A', '\\', 'Z', '_', 'n', '>', 'o', ';', '2', 'D', 'a', 'e', 'M', '9', '=',
                          '#', 'p', 'w', 'b', 't']

    def _ciphered_less_padding(self, value: str) -> str:
        return value[1:len(value) - 1]

    def _position_of_spaces(self, value: str) -> List[int]:
        return [index for index, character in enumerate(value) if character == ' ']

    def test_cipher(self):
        ciphered = apply_cipher(CipherTests._ORIGINAL_VALUE, CipherTests._CHARACTER_OPTIONS)
        self.assertEqual(len(CipherTests._ORIGINAL_VALUE) + 2, len(ciphered))
        self.assertNotEqual(self._ciphered_less_padding(ciphered), CipherTests._ORIGINAL_VALUE)

        self.assertEqual(CipherTests._ORIGINAL_VALUE, reverse_cipher(ciphered, CipherTests._CHARACTER_OPTIONS))

    def test_cipher_variance(self):
        generated = set()
        option_length = len(CipherTests._CHARACTER_OPTIONS)
        for i in range(option_length):
            ciphered = apply_cipher(CipherTests._ORIGINAL_VALUE, CipherTests._CHARACTER_OPTIONS)
            generated.add(self._ciphered_less_padding(ciphered))
        self.assertGreaterEqual(option_length * 0.95, len(generated))

    def test_cipher_without_replacing_spaces(self):
        options = CipherTests._CHARACTER_OPTIONS[:]
        options.pop(options.index(' '))
        self.assertFalse(' ' in options)

        original_space_positions = self._position_of_spaces(CipherTests._ORIGINAL_VALUE)
        ciphered = apply_cipher(CipherTests._ORIGINAL_VALUE, options)

        self.assertNotEqual(CipherTests._ORIGINAL_VALUE, ciphered)
        new_space_positions = self._position_of_spaces(self._ciphered_less_padding(ciphered))

        self.assertEqual(original_space_positions, new_space_positions)
