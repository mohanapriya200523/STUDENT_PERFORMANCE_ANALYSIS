import matplotlib.pyplot as plt
import seaborn as sns

marks = [85, 90, 78, 88]

plt.plot(marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()


sns.barplot(x=["A","B","C","D"], y=marks)
plt.title("Marks Bar Chart")
plt.show()
