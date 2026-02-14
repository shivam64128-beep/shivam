marks = []

print("Enter marks of 5 subjects (out of 100):")

for i in range(1, 6):
    value = float(input(f"Subject {i}: "))
    marks.append(value)

total = sum(marks)
percentage = (total / 500) * 100

print("Total Marks =", total)
print("Percentage =", round(percentage, 2), "%")
