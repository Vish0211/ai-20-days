import pandas as pd

 
data = {
    "Name": ["Arun", "Bala", "Charan", "Divya", "Esha"],
    "Marks": [85, 92, 78, 88, 95],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"]
}

df = pd.DataFrame(data)

 
print(" Student Data:")
print(df)

 
print("\n Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

 
print("\n Students scoring above 85:")
print(df[df["Marks"] > 85])

print("\n Sorted by Marks (High to Low):")
print(df.sort_values(by="Marks", ascending=False))


print("\n Department Wise Average Marks:")
print(df.groupby("Department")["Marks"].mean())