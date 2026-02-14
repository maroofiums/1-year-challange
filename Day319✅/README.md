# 📈 Day 319 -  Time Series Forecasting – Theory, Mathematics & Implementation

## 1. Introduction

Time Series Forecasting is the process of predicting future values based on previously observed data ordered in time.

Unlike normal regression problems, time series data has:

* Temporal dependency
* Autocorrelation
* Trend & seasonality
* Ordered observations

Example use cases:

* Sales forecasting
* Stock price prediction
* Energy demand forecasting
* Traffic prediction

---

# 2. Components of Time Series

A time series can be decomposed into:

[
Y_t = T_t + S_t + C_t + \epsilon_t
]

Where:

* (T_t) = Trend
* (S_t) = Seasonality
* (C_t) = Cyclic
* (\epsilon_t) = Noise

Understanding these components is critical before applying any model.

---

# 3. Stationarity

A time series is **stationary** if:

* Mean is constant over time
* Variance is constant
* Autocorrelation structure does not change

Many statistical models (AR, MA, ARIMA) require stationarity.

We test using:

* Augmented Dickey-Fuller (ADF Test)

If not stationary:

* Apply differencing
* Log transformation
* Detrending

---

# 4. Mathematical Models

---

## 4.1 AutoRegressive Model (AR)

### Intuition

Current value depends on its past values.

### Mathematical Form

[
Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + ... + \phi_p Y_{t-p} + \epsilon_t
]

Where:

* (p) = number of lags
* (\phi) = coefficients
* (\epsilon_t) = white noise

### Key Idea

We use past observations to predict the present.

---

## 4.2 Moving Average Model (MA)

### Intuition

Current value depends on past forecast errors.

### Mathematical Form

[
Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + ... + \theta_q \epsilon_{t-q}
]

Where:

* (q) = order of error terms
* (\theta) = coefficients

### Key Idea

Instead of past values, we use past residuals.

---

## 4.3 ARIMA Model

ARIMA = AR + I + MA

[
ARIMA(p,d,q)
]

* p = AR order
* d = differencing order
* q = MA order

If series is non-stationary:

[
Y'*t = Y_t - Y*{t-1}
]

After differencing, we apply AR + MA.

ARIMA is powerful because it handles:

* Trend
* Autocorrelation
* Noise

---

## 4.4 Exponential Smoothing

Instead of fixed weights, recent observations get more weight.

### Simple Exponential Smoothing

[
S_t = \alpha Y_t + (1-\alpha) S_{t-1}
]

Where:

* (0 < \alpha < 1)

Higher α → More importance to recent values.

---

### Holt’s Linear Trend Method

Adds trend:

[
L_t = \alpha Y_t + (1-\alpha)(L_{t-1} + T_{t-1})
]

[
T_t = \beta (L_t - L_{t-1}) + (1-\beta)T_{t-1}
]

---

### Holt-Winters (Seasonal)

Adds seasonality component.

Used when data has:

* Trend
* Seasonal pattern

---

# 5. Implementation (Python)

## 5.1 Create Demo Data

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

dates = pd.date_range(start="2022-01-01", periods=730, freq="D")
sales = 100 + 0.05*np.arange(730) + 10*np.sin(2*np.pi*np.arange(730)/30) + np.random.normal(0,3,730)

df = pd.DataFrame({"Date": dates, "Sales": sales})
df.set_index("Date", inplace=True)

df["Sales"].plot(figsize=(12,5))
plt.title("Demo Time Series")
plt.show()
```

---

## 5.2 AR Model

```python
from statsmodels.tsa.ar_model import AutoReg

train = df["Sales"][:700]
test = df["Sales"][700:]

ar_model = AutoReg(train, lags=5).fit()
ar_pred = ar_model.predict(start=len(train), end=len(train)+len(test)-1)
```

---

## 5.3 MA Model

```python
from statsmodels.tsa.arima.model import ARIMA

ma_model = ARIMA(train, order=(0,0,2)).fit()
ma_pred = ma_model.predict(start=len(train), end=len(train)+len(test)-1)
```

---

## 5.4 ARIMA Model

```python
arima_model = ARIMA(train, order=(5,1,2)).fit()
arima_pred = arima_model.predict(start=len(train), end=len(train)+len(test)-1, typ="levels")
```

---

## 5.5 Exponential Smoothing (Holt-Winters)

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

hw_model = ExponentialSmoothing(
    train,
    trend="add",
    seasonal="add",
    seasonal_periods=30
).fit()

hw_pred = hw_model.forecast(len(test))
```

---

# 6. Evaluation Metrics

### MAE

[
MAE = \frac{1}{n}\sum |y - \hat{y}|
]

### RMSE

[
RMSE = \sqrt{\frac{1}{n}\sum (y - \hat{y})^2}
]

### MAPE

[
MAPE = \frac{100}{n}\sum \left|\frac{y - \hat{y}}{y}\right|
]

---

# 7. Model Comparison

| Model        | Handles Trend        | Handles Seasonality | Requires Stationarity    |
| ------------ | -------------------- | ------------------- | ------------------------ |
| AR           | ❌                    | ❌                   | ✅                        |
| MA           | ❌                    | ❌                   | ✅                        |
| ARIMA        | ✅ (via differencing) | ❌                   | Yes (after differencing) |
| Holt-Winters | ✅                    | ✅                   | No                       |

---

# 8. Best Practices

* Always visualize data first
* Check stationarity
* Start simple (AR or Exponential Smoothing)
* Avoid overfitting with large p and q
* Compare models using RMSE

---

# 9. Conclusion

Time Series Forecasting combines:

* Mathematical modeling
* Statistical assumptions
* Practical feature engineering

AR and MA capture short-term dependencies.
ARIMA handles non-stationarity.
Exponential Smoothing works best when trend and seasonality are clear.

---
