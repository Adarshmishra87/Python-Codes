import random

words = ["apple", "baboon", "camel"]
words_length = len(words)
choose_word = random.choice(words)
# *************************************************************************************************#
display = []
word_lengths = len(choose_word)
for _ in range(word_lengths):
    display += "_"
print(display)
# **************************************************************************************************!@#
end_of_game = False

while not end_of_game:
    guess = input("enter your favorite letter?\n").lower()

    for position in range(len(choose_word)):
        letters = choose_word[position]
        if letters == guess:
            display[position] = letters
        else:
            print("not match")
    print(display)
    # else:
    #     print("Try again")
    if "_" not in display:
        end_of_game = True
        print("You win")
