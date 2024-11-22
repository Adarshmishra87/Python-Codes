# def helloji():
#     print("Hello")
#     print("kaise ho be?")
#
# helloji()

# strs=['cccc','cc','ddsex','e']
# print(sorted(strs, key=len))
#
words=["ardvark","Jimmyshay","Cartiglewek","ferdojikama"]
import  random
counts=0
display=[]
words_length=len(words)
choose_word=random.choice(words)
gueess=input("enter your favorite letter?\n").lower()



for letters in choose_word:
    if letters==gueess:
        counts+=1
        print("right")
    else:
        print("wrong")
print(counts)