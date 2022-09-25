import unittest

from ..lib import apply_versioned_cipher, reverse_versioned_cipher


class VersionedCipherTests(unittest.TestCase):

    _CHARACTER_OPTIONS_A = ['C', '4', 'Q', ']', 'v', 'z', 'O', 'T', ',', 'y', 'R', 'j', ' ', 'd', '0', 'g', '}', 'i',
                            '7', 'X', '<', '"', '8', '3', 'B', '+', "'", 'K', 'L', 'J', 'Y', 'h', '1', '@', '/', 'U',
                            'I', 'u', '{', '?', '*', 'k', '^', 'N', 'S', ':', '-', 'G', 'V', 'H', '%', 'm', 'r', 'W',
                            'q', 'l', '[', 'F', '|', '!', 'E', '$', 'f', 'x', 'P', ')', '.', 'c', '`', '(', '6', '&',
                            's', '~', '5', 'A', '\\', 'Z', '_', 'n', '>', 'o', ';', '2', 'D', 'a', 'e', 'M', '9', '=',
                            '#', 'p', 'w', 'b', 't']
    _CHARACTER_OPTIONS_B = ['k', 'R', 'D', 'N', 'f', '>', '7', '%', '{', '!', 't', 'm', 'O', 'q', '}', '#', 'U', '_',
                            'A', 'v', 'o', '[', '\\', ')', 'I', 'C', '.', 's', 'l', "'", '$', '4', 'T', '8', 'G', '~',
                            '+', '/', 'V', 'J', 'Q', '<', 'M', 'B', 'r', 'K', '=', 'n', '(', 'W', '1', '|', 'j', '2',
                            '&', '0', 'd', 'g', 'H', ':', '-', 'i', 'c', 'X', 'E', 'F', 'P', 'a', '"', '9', 'Z', '?',
                            'w', 'z', '3', 'L', '5', 'y', '@', ';', '^', ',', 'Y', 'S', 'u', 'h', 'x', '6', 'e', ' ',
                            '`', 'b', '*', ']', 'p']

    _CHARACTER_OPTIONS = {
        'A': _CHARACTER_OPTIONS_A,
        'BB': _CHARACTER_OPTIONS_B
    }

    _ORIGINAL_VALUE = 'This is a test of the versioned cipher functions.'

    def test_versioned_cipher(self):
        ciphered = apply_versioned_cipher(VersionedCipherTests._ORIGINAL_VALUE, VersionedCipherTests._CHARACTER_OPTIONS, 'BB')
        self.assertEqual(len(VersionedCipherTests._ORIGINAL_VALUE) + 4, len(ciphered))
        self.assertNotEqual(ciphered[2:len(ciphered) - 1], VersionedCipherTests._ORIGINAL_VALUE)

        unciphered = reverse_versioned_cipher(ciphered, VersionedCipherTests._CHARACTER_OPTIONS)
        self.assertEqual(VersionedCipherTests._ORIGINAL_VALUE, unciphered)

    def test_versioned_cipher_with_both_version_dont_match(self):
        cipher_1 = apply_versioned_cipher(VersionedCipherTests._ORIGINAL_VALUE, VersionedCipherTests._CHARACTER_OPTIONS, 'A')
        cipher_2 = apply_versioned_cipher(VersionedCipherTests._ORIGINAL_VALUE, VersionedCipherTests._CHARACTER_OPTIONS, 'BB')

        self.assertNotEqual(cipher_1[1:], cipher_2[1:])

    def test_reverse_versioned_cipher_with_bad_version_throws_exception(self):
        ciphered = 'C123'
        with self.assertRaises(ValueError):
            reverse_versioned_cipher(ciphered, VersionedCipherTests._CHARACTER_OPTIONS)
