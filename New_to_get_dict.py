school = [{
    # yaha pe 1 key hai 1 value teacher hai
    # fir wapis yaha pe student key hai then key classes then key standards aur value is list
    # key is color value is red
    "Principal": {
        "Teacher": {
            "Student": {
                "Classes": {
                    "Standards": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                    "Color": "Red"
                }
            }
        }
    }
}
]

def add_school_system(Principals,Standardss,Colors):
    old_school={}
    old_school["Principal"]=Principals
    old_school["Standards"]=Standardss
    old_school["Color"]=Colors
    school.append(old_school)


add_school_system("Adarsh",2,["Allahabad","Lucknow"])
print(school[1])
# print(school["Principal"])
