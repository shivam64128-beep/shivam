marks = []
student1 = int(input("enter marks here: "))
marks.append(student1)
student2 = int(input("enter marks here: "))
marks.append(student2)
student3 = int(input("enter marks here: "))
marks.append(student3)
student4 = int(input("enter marks here: "))
marks.append(student4)
student5 = int(input("enter marks here: "))
marks.append(student5)
student6 = int(input("enter marks here: "))
marks.append(student6)

marks.sort()

print(marks)

mark1 = {
    "shivam": 100,
    "rohit": 54,
    "prajjwal": 23,
}
print(mark1, type(mark1))
print(mark1["shivam"])
print(mark1.values())
print(mark1.keys())
print(mark1.items())
mark1.update({"shivam": 99, "roshni": 100})
print(mark1)
print(mark1.get("roshni"))
# print(mark1["rohit2"])  # return erorr
# print(mark1.get("rohit2"))  # print non
