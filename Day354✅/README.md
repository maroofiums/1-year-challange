# Day354 - Time Series Basics Notebook 

## 📖 Overview

This notebook demonstrates the **fundamental concepts of Time Series** in Python using a small sample dataset. It focuses on:

1. Visualizing time series data
2. Applying **moving averages** to smooth fluctuations
3. Decomposing the series into **trend, seasonal, and residual components**

This is designed as a **basic introduction** to understand patterns in time-indexed data.

---

## 🛠️ Libraries Used

* **pandas** → data handling and time-indexed series
* **matplotlib** → visualization of trends and patterns
* **statsmodels** → decomposition of time series

---

## 📊 Steps in the Notebook

### 1️⃣ Import Libraries

The notebook starts by importing necessary Python libraries.

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
```

---

### 2️⃣ Create Sample Time Series Data

* A simple dataset of 12 daily values is used.
* Dates are generated using `pd.date_range`.
* Data is stored in a pandas DataFrame with **date index**.

```python
data = [10, 12, 13, 12, 14, 15, 14, 16, 17, 16, 18, 19]
dates = pd.date_range(start='2026-01-01', periods=len(data))
df = pd.DataFrame({'value': data}, index=dates)
```

---

### 3️⃣ Plot Original Time Series

* Helps visualize **overall trend and fluctuations**.
* Each point represents a value on a specific day.

```python
plt.plot(df.index, df['value'], marker='o')
```

---

### 4️⃣ Moving Average (3-Day Window)

* Smooths short-term fluctuations to highlight the **trend**.
* Rolling window of size 3 is applied.

```python
df['MA_3'] = df['value'].rolling(3).mean()
```

* Plot shows **original values** + **moving average**.

---

### 5️⃣ Decomposition (Additive Model)

* Splits the series into **trend, seasonal, and residual components**:

```python
result = seasonal_decompose(df['value'], model='additive', period=3)
result.plot()
```

* **Trend** → smoothed long-term direction
* **Seasonal** → repeating short-term pattern
* **Residual** → remaining noise

---

### 6️⃣ Observations

* **Trend Component** shows gradual increase in values.
* **Seasonal Component** shows repeating ups and downs over the period.
* **Residual Component** is near zero (very little random noise in this small dataset).

---

## ⚡ Key Takeaways

1. Time Series is **time-indexed data** where order matters.
2. **Moving Average** is a simple method to smooth data and see trends.
3. **Decomposition** helps separate trend, seasonality, and noise for analysis.
4. Even **simple datasets** can reveal clear patterns when plotted.

---
