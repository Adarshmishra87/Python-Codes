students=input("enter our scores here:").split()
for n in range(0,len(students)):
    students[n]=int(students[n])
print(max(students))
# print(min(students))
heig=0
for score in students:
    if score>heig:
        heig=score
print(heig)