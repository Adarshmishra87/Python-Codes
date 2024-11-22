row1=[" "," "," "]
row2=[" "," "," "]
row3=[" ","8"," "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=(input("Enter your desired box? "))
horizontal=int(position[0])
vertical=int(position[1])
map[horizontal-1][horizontal-1]="X"
print(map)