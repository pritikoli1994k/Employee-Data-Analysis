import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load CSV file
data = pd.read_csv("data.csv")

# 2️⃣ Show first 2–3 lines of data
print("Data:\n", data.head())

# 3️⃣ Convert Salary & Experience columns to numeric (ignore errors like 'Asha')
data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')
data['Experience'] = pd.to_numeric(data['Experience'], errors='coerce')

# 4️⃣ Drop rows with missing values in key columns
data = data.dropna(subset=['Salary', 'Experience'])

# 5️⃣ Average Salary
average_salary = data['Salary'].mean()
print("\nAverage Salary:", average_salary)

# 6️⃣ Department-wise Average Salary
avg_salary_dept = data.groupby('Department')['Salary'].mean()
print("\nDepartment-wise Average Salary:\n", avg_salary_dept)

# 7️⃣ Bar Chart
avg_salary_dept.plot(kind='bar', color='skyblue')
plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# 8️⃣ Scatter Plot (Experience vs Salary)
plt.scatter(data['Experience'], data['Salary'], color='green')
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()

# 9️⃣ Heatmap (Correlation)
# Select only numeric columns for correlation
corr = data.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
