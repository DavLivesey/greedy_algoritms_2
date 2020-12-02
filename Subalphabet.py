

def subalphabet(letter_code, character):
    if letter_code > character:
        return

    print(chr(letter_code), end=' ')
    subalphabet(letter_code + 1, character)


if __name__ == '__main__':
    char = input()
    subalphabet(97, ord(char))
