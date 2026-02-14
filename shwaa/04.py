a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
print("the avg. is :", (a + b) / 2)

c = int(input("enter number :"))
print("squre of the number is:", c**2)

name = "shivam"
nameshort = name[0:6]
print(nameshort)
chracter1 = name[0]
print(chracter1)
print(name[1:3])
print(name[-4:-1])
print(name[:4])
print(name[1:])

name2 = "archlinux"
print(name2[0:1])
print(name2[0:2])
print(name2[0:3])
print(name2[0:4])
print(name2[0:5])
print(name2[0:6])
print(name2[0:7])
print(name2[0:8])
print(name2[0:])

name3 = "abcdefghijklmnopqrstuvwxyz"
print(name3[0:9:2])

name4 = "bigbooks"
print(len(name4))
print(name4.endswith("boobs"))
print(name4.startswith("boobs"))
print(name4.capitalize())
print(name4.upper())
print(name4.lower())

name5 = "big big boobs very big"
print(name5.replace("big", "small"))
print(name5.encode())
print(name5.find("oo"))

name6 = 'bigboobs \n\tvery bigboobs \nvery very "bigboobs"'
print(name6)

name7 = input("enter your name: ")
print(f"fuck you,{name7} ")

letter = """dear <|name|>,
you are selected!
<|date|>"""

print(letter.replace("<|name|>", "shivam").replace("<|date|>", "6-10-2004"))
