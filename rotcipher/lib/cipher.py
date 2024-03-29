from typing import List
import random
from .cipher_exception import CipherException


_CIPHER_ATTEMPTS_BEFORE_QUITTING = 100  # pragma: no mutate


def _validate_character_options(character_options: List[str]):
    if len(character_options) == 0:
        raise ValueError('The character_options must contain at least one element.')
    for character in character_options:
        character_length = len(character)
        if character_length != 1:
            raise ValueError('All entries in the character_options list must be a single character. '
                             f'Character [{character}] has a length of [{character_length}].')


def _compute_next_index(character: str, index: int, shift_by: int, shift_direction: int, character_options: List[str])\
        -> int:
    """
    Calculates the next index which a character from the character_options list should be pulled to be used
    to replace the 'character' value from the source string.

    :param character: The current character that is being substituted.
    :param index: The index of the 'character' as it appears in the string that is being substituted. Used to reduce
        the likelihood that repeated characters in the input string being substituted will be substituted with different
        but also repeating characters.
    :param shift_by: The number of positions to shift by. This number should always be a positive.
    :param shift_direction: The direction to shift by. Can be either 1 or -1.
    :param character_options: The array of characters used to compute the index.
    :return: The index of the character in the character_options list that should be used to replace the input
        'character' from the source string that is being substituted.
    """

    if character not in character_options:
        return -1
    return (character_options.index(character) + (shift_by * index * shift_direction)) % len(character_options)


def _apply_rot(value: str, shift_by: int, character_options: List[str], reverse_modifier=1) -> str:
    """
    Substitutes the characters in the input string with characters pulled from the randomly sorted
    character_options list based on the shift_by and reverse_modifier values.

    :param value: The input string which will be substituted.
    :param shift_by: The amount to shift, or rotate, by.
    :param reverse_modifier: A modifier to be used to indicate whether we are applying the cipher to the given
        input string or reversing. Should have a value of either 1 or -1.
    :param character_options: The array of characters which the characters in the value string will be mapped to.
    :return: The ciphered string with all the characters from the 'value' string substituted with values pulled
        from the character_options list.
    """

    def next_character_option(index: int, fallback: str) -> str:
        # -1 means the original character from the input string could not be found in the character option list
        # and therefore needs to be skipped.
        if index == -1:
            return fallback
        return character_options[index]

    if shift_by % 2 == 0:
        shift_direction = -1 * reverse_modifier
    else:
        shift_direction = reverse_modifier
    indexes = [_compute_next_index(value[i], i, shift_by, shift_direction, character_options) for i in range(len(value))]
    return ''.join(next_character_option(computed_index, value[i]) for i, computed_index in enumerate(indexes))


def apply_cipher(value: str, character_options: List[str]) -> str:
    """
    Applies the customized rotational substitution cipher to the input value.

    This cipher works by:
    1. Generating two padding characters that act like a pseudo-random initialization vector.
    2. Converting the padding characters to a numeric value to be used to determine the rotation amount.
    3. Substituting the characters in the source string with the rotated characters pulled from the randomly ordered
    character_options list.
    4. Pre-pending and appending the padding characters in step one to the string generated in step 3.

    This function will continuously loop until a ciphered representation of the value string is generated such that the
    ciphered string, without the padding characters, is not strictly equal to the input value string.

    Additionally, this function will skip any characters in the input value string if the input character cannot
    be found within the list of character options.

    :param value: The string which the substitution cipher will be applied to.
    :param character_options: The list of characters which the characters from the input value string will ultimately
        be mapped to.
    :return: A string representation of the ciphered text including some padding characters used in calculating
        the rotation amount and direction.
    """

    _validate_character_options(character_options)

    for i in range(_CIPHER_ATTEMPTS_BEFORE_QUITTING):
        left_padding = random.choice(character_options)
        right_padding = random.choice(character_options)
        shift_by = character_options.index(left_padding) + character_options.index(right_padding)
        shifted = _apply_rot(value, shift_by, character_options)
        if shifted != value:
            return left_padding + shifted + right_padding
    raise CipherException(f'After {_CIPHER_ATTEMPTS_BEFORE_QUITTING} attempts apply_cipher was not able to generate '
                          f'a ciphered value different from the original.')


def _value_without_padding_characters(value: str) -> str:
    return value[1:-1]


def reverse_cipher(value: str, character_options: List[str]) -> str:
    """
    Reverses the customized rotational substitution cipher that was previously applied to the input value string.

    In order for this to succeed the character_options needs to strictly match the character_options used when
    invoking the apply_cipher function.

    :param value: The ciphered string which is to have the substitution process reversed.
    :param character_options: The list of characters which the characters from the input value string will ultimately
        be mapped to.
    :return: The original string before the cipher was applied.
    """

    _validate_character_options(character_options)

    if len(value) == 0:
        raise ValueError('The ciphered value must have a minimum length of 1.')

    left_padding = value[0]
    right_padding = value[-1]

    if left_padding not in character_options:
        raise CipherException(f'Could not reverse cipher on input string. Padding character [{left_padding}] could not be '
                              f'found')

    shift_by = character_options.index(left_padding) + character_options.index(right_padding)
    value_without_padding = _value_without_padding_characters(value)
    return _apply_rot(value_without_padding, shift_by, character_options, -1)
