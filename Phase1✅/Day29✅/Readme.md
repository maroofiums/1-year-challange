# Day-29

Great! Here's a concise guide to **Data Visualization using Matplotlib and Seaborn** – two of the most popular libraries in Python for plotting.

---

## 🔹 1. **Matplotlib (Foundation of Python Visualization)**

### 📦 Installation

```bash
pip install matplotlib
```

### 📊 Basic Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
```

### 📈 Other Common Plots

```python
# Bar Chart
plt.bar(x, y)

# Scatter Plot
plt.scatter(x, y)

# Histogram
data = [1, 1, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data)

# Pie Chart
labels = ['A', 'B', 'C']
sizes = [30, 45, 25]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
```

### 🎨 Customizations

```python
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.xlim(0, 5)
plt.ylim(0, 35)
```

---

## 🔹 2. **Seaborn (Built on Matplotlib, More Elegant)**

### 📦 Installation

```bash
pip install seaborn
```

### 🔧 Setup

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### 📚 Use Built-in Datasets

```python
df = sns.load_dataset('tips')  # dataset about restaurant tips
print(df.head())
```

### 📊 Common Plots

```python
# Histogram with KDE
sns.histplot(df['total_bill'], kde=True)

# Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=df)

# Box Plot
sns.boxplot(x='day', y='total_bill', data=df)

# Violin Plot
sns.violinplot(x='day', y='total_bill', data=df)

# Heatmap (for correlation)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Pairplot (multiple scatter plots)
sns.pairplot(df)
```

### 🎨 Themes

```python
sns.set_style("darkgrid")  # Options: white, dark, whitegrid, darkgrid, ticks
```

---

## 🧠 Tips for Beginners

* Start with Matplotlib to understand basic plotting concepts.
* Use Seaborn for cleaner and more statistical plots.
* Combine both for best results: Seaborn for plots, Matplotlib for fine-tuning.

---

## 📘 Mini Practice Project Idea

**Dataset:** Titanic (available in Seaborn)

**Tasks:**

* Plot survival rate using `sns.countplot()`
* Visualize age distribution by gender with `sns.histplot()`
* Create a heatmap of feature correlations

---

