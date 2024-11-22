import math
height=int(input("enter your height\n"))
weight=int(input("enter your weight\n"))
canns=int(input("enter your cans\n"))

def calculate(height,weight,cans):
    area=height*weight
    no_of_cans=math.ceil(area/cans)
    print(f"no of cans are {no_of_cans} that's it.")

calculate(height,weight,canns)