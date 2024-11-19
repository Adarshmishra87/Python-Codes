letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

direction = input("Type you wanted to encoded are decoded the code:?\n")
plain_text = input("Enter your text here:\n").lower()
shifts = int(input("enter your shift number here:\n"))


def encrypt(plain, shift1):
    cipher = ""
    for english_letters in plain:
        positions = letters.index(english_letters)
        new_positions = positions + shift1
        new_letters = letters[new_positions]
        cipher += new_letters
    print(cipher)


def decrypt(cipher, shift1):
    cipher_text = ""
    for english_letters in cipher:
        positions = letters.index(english_letters)
        new_positions = positions - shift1
        cipher_text += letters[new_positions]
    print(cipher_text)


if direction == "encode":
    encrypt(plain=plain_text, shift1=shifts)
elif direction=="decode":
    decrypt(cipher=plain_text, shift1=shifts)
