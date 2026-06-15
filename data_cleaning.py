import pandas as pd

data = {
    "Name": ["Arun", "Bala", None, "Divya", "Arun"],
    "Marks": [85, None, 78, 88, 85],
    "Department": ["CSE", "IT", "CSE", None, "CSE"]
}

df = pd.DataFrame(data)

print("📊 Original Data:")
print(df)

 
print("\n Missing Values:")
print(df.isnull().sum())

 
df["Name"].fillna("Unknown", inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Department"].fillna("Not Assigned", inplace=True)

print("\n After Filling Missing Values:")
print(df)

 
df = df.drop_duplicates()

print("\n After Removing Duplicates:")
print(df)