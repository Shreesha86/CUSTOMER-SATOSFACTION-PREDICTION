import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('custSup_cleaned.csv')

# Set plot style
sns.set(style="whitegrid")

# 1. Distribution of target variable (Customer Satisfaction Rating)
plt.figure(figsize=(8,5))
sns.countplot(x='Customer Satisfaction Rating', data=df)
plt.title('Distribution of Customer Satisfaction Ratings')
plt.show()

# 2. Distribution of Customer Age
plt.figure(figsize=(8,5))
sns.histplot(df['Customer Age'], bins=30, kde=True)
plt.title('Customer Age Distribution')
plt.show()

# 3. Satisfaction rating by Customer Gender
plt.figure(figsize=(8,5))
sns.boxplot(x='Customer Gender', y='Customer Satisfaction Rating', data=df)
plt.title('Satisfaction Rating by Gender')
plt.show()

# 4. Average satisfaction rating by Product Purchased
plt.figure(figsize=(10,6))
avg_rating_product = df.groupby('Product Purchased')['Customer Satisfaction Rating'].mean().sort_values()
avg_rating_product.plot(kind='barh', color='skyblue')
plt.xlabel('Average Satisfaction Rating')
plt.title('Average Satisfaction Rating by Product Purchased')
plt.show()

# 5. Correlation heatmap for numeric variables
plt.figure(figsize=(8,6))
numeric_cols = ['Customer Age', 'Response Delay Minutes', 'Resolution Time Hours', 'Customer Satisfaction Rating']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation between Numeric Features')
plt.show()
