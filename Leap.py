year=int(input())
if year%400==0:
    if year%4==0:
        print("Leap year")
    else:
        print("Not a Leap year")
elif year%100!=0:
    print("NOT exist")
