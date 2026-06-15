import csv

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)

    maths_marks = []

    for row in reader:
        maths_marks.append(int(row["Maths"]))

average = sum(maths_marks) / len(maths_marks)
highest = max(maths_marks)
lowest = min(maths_marks)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)