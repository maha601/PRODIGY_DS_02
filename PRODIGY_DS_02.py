import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    "gender": ["female", "male", "female", "male", "female", "male", "female", "male", "female", "male"],
    "parental_level_of_education": ["bachelor", "some college", "master", "associate", "high school", "some college", "bachelor", "high school", "associate", "master"],
    "math_score": [72, 69, 90, 47, 76, 71, 88, 40, 64, 55],
    "reading_score": [72, 90, 95, 57, 78, 70, 95, 43, 67, 58],
    "writing_score": [74, 88, 93, 44, 75, 65, 92, 39, 63, 55]
}

df = pd.DataFrame(data)

# Display first few rows
print("First 5 rows:")
print(df.head())

# Data Info
print("\nInfo:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary:")
print(df.describe())

# Gender count
sns.countplot(data=df, x='gender')
plt.title("Student Gender Distribution")
plt.show()

# Average score by gender
df.groupby("gender")[["math_score", "reading_score", "writing_score"]].mean().plot(kind="bar")
plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.show()

# Correlation heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df[["math_score", "reading_score", "writing_score"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation between Subjects")
plt.show()