# age=int(input("enter your age"))
# if age>18 and age>10:
#     print("Yes U can")
# else:
#     print("Better luck next time")

# name="adarsh"
# print(name.upper())
# print(name.count("a"))
import random
name=input(("enter her name:\n"))
name1=input(("enter her name1:\n"))

count=name1+name
lower=count.lower()
t=lower.count("t")
r=lower.count("r")
u=lower.count("u")
e=lower.count("e")
true=t+r+u+e
l=lower.count("l")
o=lower.count("o")
v=lower.count("v")
e=lower.count("e")
love=l+o+v+e
love_Score=int(str(true)+str(love))
c=random.randint(1,100)



if (love_Score <c) or (love_Score>c):
    print(f"Your score is {love_Score}, you go together like coke and mentos.")
elif (love_Score>=c) and (love_Score<=c):
    print(f"Your score is {love_Score}, you go together like cake and pastry.")
else:
    print(f"your score is {love_Score}")