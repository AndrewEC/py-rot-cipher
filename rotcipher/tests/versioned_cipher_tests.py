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

    _OPTION_A = 'A'
    _OPTION_B = 'AB'

    _CHARACTER_OPTIONS = {
        _OPTION_A: _CHARACTER_OPTIONS_A,
        _OPTION_B: _CHARACTER_OPTIONS_B
    }

    _ORIGINAL_VALUE = 'This is a test of the versioned cipher functions.'

    def _ciphered_less_padding(self, ciphered: str) -> str:
        return ciphered[3:len(ciphered) - 1]

    def test_versioned_cipher(self):
        ciphered = apply_versioned_cipher(VersionedCipherTests._ORIGINAL_VALUE, VersionedCipherTests._CHARACTER_OPTIONS, VersionedCipherTests._OPTION_B)
        self.assertEqual(len(VersionedCipherTests._ORIGINAL_VALUE) + 4, len(ciphered))
        self.assertNotEqual(self._ciphered_less_padding(ciphered), VersionedCipherTests._ORIGINAL_VALUE)

        unciphered = reverse_versioned_cipher(ciphered, VersionedCipherTests._CHARACTER_OPTIONS)
        self.assertEqual(VersionedCipherTests._ORIGINAL_VALUE, unciphered)

    def test_reverse_versioned_cipher_with_bad_version_throws_exception(self):
        ciphered = 'C123'
        with self.assertRaises(ValueError) as error:
            reverse_versioned_cipher(ciphered, VersionedCipherTests._CHARACTER_OPTIONS)
        self.assertTrue(str(error.exception).startswith('Could not determine'))

    def test_reverse_versioned_cipher_with_missmatched_versions_produced_incorrect_result(self):
        reverse_options = {
            VersionedCipherTests._OPTION_A: VersionedCipherTests._CHARACTER_OPTIONS_B,
            VersionedCipherTests._OPTION_B: VersionedCipherTests._CHARACTER_OPTIONS_A
        }

        ciphered = apply_versioned_cipher(VersionedCipherTests._ORIGINAL_VALUE, VersionedCipherTests._CHARACTER_OPTIONS, VersionedCipherTests._OPTION_B)
        unciphered = reverse_versioned_cipher(ciphered, reverse_options)
        self.assertNotEqual(VersionedCipherTests._ORIGINAL_VALUE, unciphered)

    def test_apply_versioned_cipher_with_invalid_version_raises_value_error(self):
        with self.assertRaises(ValueError):
            apply_versioned_cipher(VersionedCipherTests._ORIGINAL_VALUE, VersionedCipherTests._CHARACTER_OPTIONS, 'D')

    def test_reverse_version_cipher_with_zero_length_value_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            reverse_versioned_cipher('', VersionedCipherTests._CHARACTER_OPTIONS)
