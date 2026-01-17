import pandas as pd
import matplotlib.pyplot as plt

# Load dataset with TAB separator
df = pd.read_csv("StudentsPerformance.csv")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print(df.columns)  # check column names

# Calculations
avg_math = df["math_score"].mean()
avg_reading = df["reading_score"].mean()
avg_writing = df["writing_score"].mean()

print("Average Math Score:", avg_math)
print("Average Reading Score:", avg_reading)
print("Average Writing Score:", avg_writing)

df["overall_score"] = (df["math_score"] + df["reading_score"] + df["writing_score"]) / 3

pass_students = df[df["overall_score"] >= 40].shape[0]
total_students = df.shape[0]
print("\nPass Percentage:", (pass_students / total_students) * 100, "%")

gender_performance = df.groupby("gender")["overall_score"].mean()
print("\nGender Based Performance:\n", gender_performance)

subjects = ["Math", "Reading", "Writing"]
averages = [avg_math, avg_reading, avg_writing]

plt.bar(subjects, averages)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()
