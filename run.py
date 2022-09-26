import click

from rotcipher import apply_cipher, reverse_cipher, apply_versioned_cipher, reverse_versioned_cipher


CHARACTER_OPTIONS_A = ['C', '4', 'Q', ']', 'v', 'z', 'O', 'T', ',', 'y', 'R', 'j', ' ', 'd', '0', 'g', '}', 'i', '7', 'X', '<', '"', '8', '3', 'B', '+', "'", 'K', 'L', 'J', 'Y', 'h', '1', '@', '/', 'U', 'I', 'u', '{', '?', '*', 'k', '^', 'N', 'S', ':', '-', 'G', 'V', 'H', '%', 'm', 'r', 'W', 'q', 'l', '[', 'F', '|', '!', 'E', '$', 'f', 'x', 'P', ')', '.', 'c', '`', '(', '6', '&', 's', '~', '5', 'A', '\\', 'Z', '_', 'n', '>', 'o', ';', '2', 'D', 'a', 'e', 'M', '9', '=', '#', 'p', 'w', 'b', 't']
CHARACTER_OPTIONS_B = ['k', 'R', 'D', 'N', 'f', '>', '7', '%', '{', '!', 't', 'm', 'O', 'q', '}', '#', 'U', '_', 'A', 'v', 'o', '[', '\\', ')', 'I', 'C', '.', 's', 'l', "'", '$', '4', 'T', '8', 'G', '~', '+', '/', 'V', 'J', 'Q', '<', 'M', 'B', 'r', 'K', '=', 'n', '(', 'W', '1', '|', 'j', '2', '&', '0', 'd', 'g', 'H', ':', '-', 'i', 'c', 'X', 'E', 'F', 'P', 'a', '"', '9', 'Z', '?', 'w', 'z', '3', 'L', '5', 'y', '@', ';', '^', ',', 'Y', 'S', 'u', 'h', 'x', '6', 'e', ' ', '`', 'b', '*', ']', 'p']

CHARACTER_OPTIONS = {
    'A': CHARACTER_OPTIONS_A,
    'B': CHARACTER_OPTIONS_B
}


@click.command('apply')
@click.argument('value')
def apply(value: str):
    print(apply_cipher(value, CHARACTER_OPTIONS_A))


@click.command('reverse')
@click.argument('value')
def reverse(value: str):
    print(reverse_cipher(value, CHARACTER_OPTIONS_A))


@click.command('apply-versioned')
@click.argument('version', type=click.Choice(list(CHARACTER_OPTIONS.keys())))
@click.argument('value')
def apply_versioned(version: str, value: str):
    print(apply_versioned_cipher(value, CHARACTER_OPTIONS, version))


@click.command('reverse-versioned')
@click.argument('value')
def reverse_versioned(value: str):
    print(reverse_versioned_cipher(value, CHARACTER_OPTIONS))


@click.group()
def main():
    pass


main.add_command(apply)
main.add_command(reverse)
main.add_command(apply_versioned)
main.add_command(reverse_versioned)


if __name__ == '__main__':
    main()
