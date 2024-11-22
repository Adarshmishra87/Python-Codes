stubs = input("enter your list: ").split()
sum = 0
for n in range(0, len(stubs)):
    stubs[n] = int(stubs[n])
    sum += stubs[n]
calcu = sum / len(stubs)
print(stubs)
print("Sum of total list is:",sum)
print("Height of average students are:",calcu)
