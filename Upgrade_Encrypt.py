letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q ', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', ' *',
           ' ( )', '-', '_', '=', '+']

should_continue = True
while should_continue:
    direction = input("Type you wanted to encode are decode the code:?\n")
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
                end_text += char
        print(end_text)


    cipher_gang(start_text=plain_text, shift1=shifts, cipher_direction=direction)
    result = input(f"If you wanted to Continue again type 'yes' Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("GoodBye")
