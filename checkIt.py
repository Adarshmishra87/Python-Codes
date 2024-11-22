n = int(input("Enter a number:\n"))


def checkPrime(n):
    isprime = True
    for i in range(2, n):
        if n % 2 == 0:
            isprime = False
    if isprime:
        print("Prime number")
    else:
        print("Not prime")

checkPrime(n)