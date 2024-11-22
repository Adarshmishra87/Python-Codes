letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q ', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

direction = input("Type you wanted to encoded are decoded the code:?\n")
plain_text = input("Enter your text here:\n").lower()
shifts = int(input("enter your shift number here:\n"))


def cipher_gang(start_text, shift1, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift1 *= -1
    for char in start_text:
        if char in letters:
         position = letters.index(char)
         new_position = (position + shift1) % 26
         end_text += letters[new_position]
        else:
            end_text+=char
    print(end_text)


cipher_gang(start_text=plain_text, shift1=shifts, cipher_direction=direction)
