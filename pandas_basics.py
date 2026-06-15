import pandas as pd

data = {
    "Name": ["Priya", "Ravi", "Anu"],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data)

print(df[df["Marks"] > 90])