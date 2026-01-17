import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Priya"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
print("Average Marks:", df["Marks"].mean())
