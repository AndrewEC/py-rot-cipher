from typing import List, Dict

from .cipher import apply_cipher, reverse_cipher


def apply_versioned_cipher(value: str, character_options: Dict[str, List[str]], version: str) -> str:
    """
    This works much like the apply_cipher function except that the result of this function will, in addition to the
    padding characters appended by the apply_cipher function, pre-pend an additional character to the resulting ciphered
    string. This additional character will be used to represent the version of the cipher applied.

    This function will essentially take the input version, use it as a key to pull a randomly ordered character list
    from the character options dictionary, and pass the value and character list to the apply_cipher function. After
    the apply_cipher is complete this will prepend the version value to the front of the ciphered string and
    return the final result.

    :param value: The input string to be ciphered.
    :param character_options: A dictionary of all the randomly ordered character options with an associated version
    string.
    :param version: Indicates which random character option list to the pull from the dictionary of character options.
    :return: A ciphered representation of the input value string.
    """

    if version not in character_options:
        raise ValueError(f'The provided version [{version}] cannot be found in the provided dictionary of character options.')
    ciphered = apply_cipher(value, character_options[version])
    return version + ciphered


def _determine_version(value: str, available_versions: List[str]) -> str | None:
    value_length = len(value)
    for version in sorted(available_versions, key=len, reverse=True):
        if len(version) > value_length:
            continue
        if value.startswith(version):
            return version
    return None


def reverse_versioned_cipher(value: str, character_options: Dict[str, List[str]]) -> str:
    """
    Works much like the reverse_cipher function with the added step in which this function will pull the
    leading characters from the value string and use it as the version indicator to pull a random character option
    list from the dictionary of character options.

    The remaining characters, input value less the first character, will be passed to the reverse_cipher function
    along with the random character list pulled in the aforementioned step.

    :param value: The string previously ciphered using the apply_ciphered_versioned function.
    :param character_options: A dictionary containing a series of random character lists to pull from based on the
    version value pulled from the input value string.
    :return: The original, un-ciphered, version of the input value string.
    """

    character_option_keys = list(character_options.keys())
    if len(value) == 0:
        raise ValueError('The value parameter must contain at least one character.')
    version = _determine_version(value, character_option_keys)
    if version is None:
        raise ValueError('Could not determine the appropriate version to use for the input string. '
                         'This string may not have been properly ciphered or the version originally used to apply '
                         'the rotational cipher is not available as a key in the character_options dictionary.')
    ciphered = value[len(version):]
    return reverse_cipher(ciphered, character_options[version])
