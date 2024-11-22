school = {
    # yaha pe 2 key hai 1 value teacher hai
    # fir wapis yaha pe student key hai then key classes then key standards aur value is list
    # key is color value is red
    "Principal": "Teacher",
    "Student": {
        "Classes": {
            "Standards": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            "Color": "Red"
        }
    }
}

print(school["Principal"])
