# Day 303

## **1️⃣ Two Sum (Easy)**

**Problem:**
Given an array `nums` and a target `target`, return indices of two numbers that add up to the target.

**Example:**

```text
nums = [2,7,11,15], target = 9
Output: [0,1]  # 2+7=9
```

**Step-by-Step Approach:**

1. Use a dictionary to store numbers and their indices
2. Loop through the array
3. Check if `target - num` exists in dict
4. If yes → return indices

**Python Code:**

```python
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
```

**Time Complexity:** O(n) ✅
**Space Complexity:** O(n) ✅

---

## **2️⃣ Maximum Subarray (Easy – Sliding Window / Kadane’s)**

**Problem:**
Find the contiguous subarray with the **largest sum**.

**Example:**

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6  # [4,-1,2,1]
```

**Step-by-Step Approach (Kadane’s Algorithm):**

1. Keep track of current sum
2. If current sum < 0 → reset to 0
3. Update max sum if current sum > max

**Python Code:**

```python
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = 0
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum
```

**Time Complexity:** O(n) ✅
**Space Complexity:** O(1) ✅

---

## **3️⃣ Valid Parentheses (Easy – Stack)**

**Problem:**
Check if a string with `()[]{}` is **valid**. Every opening must have a closing in correct order.

**Example:**

```text
s = "({[]})"
Output: True
```

**Step-by-Step Approach:**

1. Use a stack
2. Push opening brackets
3. When closing bracket appears → check stack top
4. If matches → pop, else → invalid

**Python Code:**

```python
def isValid(s):
    stack = []
    mapping = {")":"(", "}":"{", "]":"["}
    for char in s:
        if char in mapping.values():  # opening
            stack.append(char)
        else:  # closing
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack
```

**Time Complexity:** O(n) ✅
**Space Complexity:** O(n) ✅

---