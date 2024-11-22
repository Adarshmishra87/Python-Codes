


name=input("Enter your name\n")
bid=int(input("Enter your Bid price\n"))
name2=input("Enter your name\n")
bid2=int(input("Enter your Bid price\n"))
dicts={name:bid,name2:bid2}
if dicts[name]<dicts[name2]:
    print(f"{name2},{bid2}")
else:
    print(f"{name},{bid}")

