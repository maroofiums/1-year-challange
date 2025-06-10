# Day 9

Sure, here's a **beginner-friendly tutorial** on **Data Visualization with Matplotlib and Seaborn** — including setup, examples, and practice tasks. This will walk you through step by step.

---

## 🎓 Data Visualization Tutorial: **Matplotlib & Seaborn**

---

### 🧰 Step 1: Install the Libraries

Make sure you have both libraries installed:

```bash
pip install matplotlib seaborn pandas
```

---

### 📁 Step 2: Import the Libraries

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

---

## 📈 Matplotlib Tutorial

### 📌 1. Line Plot

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, color='blue', marker='o', linestyle='-')
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()
```

---

### 📌 2. Bar Chart

```python
fruits = ['Apple', 'Banana', 'Orange']
sales = [30, 50, 20]

plt.bar(fruits, sales, color='orange')
plt.title("Fruit Sales")
plt.ylabel("Quantity Sold")
plt.show()
```

---

### 📌 3. Pie Chart

```python
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 25, 15, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Programming Language Popularity")
plt.show()
```

---

## 🌈 Seaborn Tutorial

Let’s use a built-in dataset for easy practice.

### 📌 1. Load Dataset

```python
tips = sns.load_dataset("tips")
print(tips.head())
```

---

### 📌 2. Scatter Plot

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Tips vs Total Bill")
plt.show()
```

---

### 📌 3. Histogram with KDE

```python
sns.histplot(tips["total_bill"], kde=True)
plt.title("Histogram of Total Bills")
plt.show()
```

---

### 📌 4. Box Plot

```python
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Box Plot by Day and Gender")
plt.show()
```

---

### 📌 5. Heatmap (Correlation Matrix)

```python
correlation = tips.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

---

## 📝 Practice Tasks

1. **Matplotlib Tasks:**

   * Create a bar chart of 5 favorite movies with their ratings.
   * Create a line chart showing temperature over a week.
   * Create a pie chart of your daily activities.

2. **Seaborn Tasks:**

   * Load the `iris` dataset and create a pairplot.
   * Use the `tips` dataset to:

     * Plot a violin plot of tips by day.
     * Plot a bar plot of average tip by smoker/non-smoker.

---

## 🎁 Bonus: Combining Matplotlib & Seaborn

You can use both together:

```python
sns.set(style="whitegrid")
sns.barplot(data=tips, x="day", y="total_bill", palette="muted")
plt.title("Average Bill per Day")
plt.show()
```

---

Would you like this tutorial as a **PDF or Jupyter Notebook** to download? Or do you want a project idea to apply these skills?
