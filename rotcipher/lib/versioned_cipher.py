from typing import List, Dict

from .cipher import apply_cipher, reverse_cipher


def _validate_versions(available_versions: List[str]):
    version_count = len(available_versions)
    for i in range(version_count):
        for j in range(version_count):
            if i == j:
                continue
            if available_versions[i] == available_versions[j]:
                raise ValueError(f'An invalid set of character options were provided. Found two identical versions of [{available_versions[i]}] at [{i}] and [{j}]')


def apply_versioned_cipher(value: str, character_options: Dict[str, List[str]], version: str) -> str:
    """
    This works much like the apply_cipher function except that it prepends a version indicator to the front of the
    ciphered string.

    This function will essentially take the input version value, use it as a key to pull a character list from the
    character options dictionary, and pass the value and character list to the apply_cipher function. After
    the apply_cipher is complete this will prepend the version value to the front of the ciphered string and
    return the final result.

    :param value: The input string to be ciphered.
    :param character_options: A dictionary of all the randomly associated character options with an associated version string.
    :param version: Indicates which random character option list to the pull from the dictionary of character options.
    :return: A ciphered representation of the input value string.
    """
    _validate_versions(list(character_options.keys()))
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
    leading character from the value string and use it as the version indicator to pull a random character option
    list from the dictionary of character options.

    The remaining characters, input value less the first character, will be passed to the reverse_cipher function
    along with the appropriate random character list pulled from the character_options dictionary.

    :param value: The string previously ciphered using the apply_ciphered_versioned function.
    :param character_options: A dictionary containing a series of random character lists to pull from based on the
    version value pulled from the input value string.
    :return: The original, un-ciphered, version of the input value string.
    """
    _validate_versions(list(character_options.keys()))
    if len(value) == 0:
        raise ValueError('The value parameter must contain at least one character.')
    version = _determine_version(value, list(character_options.keys()))
    if version is None:
        raise ValueError('Could not determine the appropriate version to use for the input string.')
    ciphered = value[len(version):]
    return reverse_cipher(ciphered, character_options[version])