import click

from rotcipher import apply_cipher, reverse_cipher


CHARACTER_OPTIONS = ['C', '4', 'Q', ']', 'v', 'z', 'O', 'T', ',', 'y', 'R', 'j', ' ', 'd', '0', 'g', '}', 'i', '7', 'X', '<', '"', '8', '3', 'B', '+', "'", 'K', 'L', 'J', 'Y', 'h', '1', '@', '/', 'U', 'I', 'u', '{', '?', '*', 'k', '^', 'N', 'S', ':', '-', 'G', 'V', 'H', '%', 'm', 'r', 'W', 'q', 'l', '[', 'F', '|', '!', 'E', '$', 'f', 'x', 'P', ')', '.', 'c', '`', '(', '6', '&', 's', '~', '5', 'A', '\\', 'Z', '_', 'n', '>', 'o', ';', '2', 'D', 'a', 'e', 'M', '9', '=', '#', 'p', 'w', 'b', 't']


@click.command()
@click.argument('value')
def apply(value: str):
    print(apply_cipher(value, CHARACTER_OPTIONS))


@click.command()
@click.argument('value')
def reverse(value: str):
    print(reverse_cipher(value, CHARACTER_OPTIONS))


@click.group()
def main():
    pass


main.add_command(apply)
main.add_command(reverse)


if __name__ == '__main__':
    main()
