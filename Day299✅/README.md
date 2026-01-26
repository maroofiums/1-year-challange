# Day299 - Customer Login Streak Analysis

## Problem Description

Given a list of customer login records with `customer_id` and `login_day`, the goal is to find the customer with the longest consecutive login streak and return the `customer_id` along with the streak length.

## Example

**Input:**

```python
logins = [
    (101, 1), (102, 1), (101, 2),
    (101, 3), (102, 4), (103, 5), (101, 10)
]
```

**Output:**

```python
(101, 3)
```

**Explanation:**

* Customer 101 logged in days [1, 2, 3, 10] → streak 3
* Customer 102: [1, 4] → streak 1
* Customer 103: [5] → streak 1

## Approach / Logic

1. Perform exploratory data analysis (EDA) to understand patterns.
2. Group login days by `customer_id`.
3. Sort login days for each customer.
4. Calculate consecutive streaks by comparing current day with previous day.
5. Track the maximum streak length across all customers.
6. Handle edge cases like single-day logins or multiple customers with same streak.

## Solution (Python Code)

```python
from collections import defaultdict

def longest_login_streak(logins):
    streaks = defaultdict(list)
    for cid, day in logins:
        streaks[cid].append(day)
    
    max_streak = 0
    customer_id = None
    
    for cid, days in streaks.items():
        days.sort()
        streak = 1
        local_max = 1
        for i in range(1, len(days)):
            if days[i] == days[i-1] + 1:
                streak += 1
                local_max = max(local_max, streak)
            else:
                streak = 1
        if local_max > max_streak:
            max_streak = local_max
            customer_id = cid
            
    return customer_id, max_streak

# Example Run
logins = [
    (101, 1), (102, 1), (101, 2),
    (101, 3), (102, 4), (103, 5), (101, 10)
]

print(longest_login_streak(logins))  # Output: (101, 3)
```

## Key Points / Notes

* Used `defaultdict` to group login days by customer.
* Sorting ensures correct consecutive streak calculation.
* Optimized for O(N log N) per customer due to sorting.
* Can be further optimized using sets for O(N) overall.
* Clear, modular, and readable code suitable for portfolio or interview discussion.

## Potential Improvements

* For very large datasets, consider **streaming logs** instead of loading all in memory.
* Visualize login streaks using matplotlib for reporting.
* Extend function to handle multiple customers with same max streak.

## Interview Questions & Answers

**Q1: How would you handle missing login data or inconsistencies?**

> I would first check for missing values or duplicates. Missing `login_day` could be imputed if approximate info exists, or those records could be dropped. Duplicates should be removed to ensure accurate streak calculation.

**Q2: What is the time complexity of your solution?**

> Grouping is O(N), sorting each customer's logins is O(M log M) per customer (where M is number of logins), and streak calculation is O(M). Overall complexity is O(N + sum(M_i log M_i)).

**Q3: How would you optimize for very large datasets?**

> Use sets for faster lookup to get consecutive streaks in O(N) per customer. For distributed data, consider processing each customer separately using Spark or Dask.

**Q4: How would you handle multiple customers with the same max streak?**

> Maintain a list of customers with the current max streak and return all of them if needed.

**Q5: How would you explain overfitting in this context if predicting future streaks?**

> Overfitting occurs if a model learns patterns specific only to the current month's data. To prevent it, use cross-validation on historical months, regularization in predictive models, and ensure features are generalized, not memorized.
