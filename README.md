# LeetCode-1365


---

### 📌 Problem Recap (LeetCode 1365):

Given a list `nums`, for each number, return **how many numbers in the list are smaller than it**.

---

### ✅ Your Code:

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        ans = []
        sorted_num = sorted(nums)
```

* `dic = {}`: This will store the **first index** of each unique number from the sorted list.
* `ans = []`: This will hold the final answer.
* `sorted_num = sorted(nums)`: Sorts the input list. Why? Because in a sorted list, the **index of a number** equals how many numbers are smaller than it.

---

```python
        for i in range(len(sorted_num)):
            if sorted_num[i] not in dic:
                dic[sorted_num[i]] = i
```

* This loop builds a dictionary where:

  * **key** = number
  * **value** = index (i.e., how many numbers are smaller than it)
* It **only stores the first occurrence** of each number to handle duplicates correctly.

Example:
If `nums = [8, 1, 2, 2, 3]`, then
`sorted_num = [1, 2, 2, 3, 8]`
Then `dic = {1: 0, 2: 1, 3: 3, 8: 4}`
(For `2`, it stores index `1` — meaning one number is smaller.)

---

```python
        for num in nums:
            ans.append(dic[num])
```

* For each original number in `nums`, look up its “how many numbers are smaller” value from `dic` and append it to `ans`.

---

```python
        return ans
```

* Returns the final list of answers.

---

### 🧠 Example Walkthrough:

Input:

```python
nums = [8, 1, 2, 2, 3]
```

1. `sorted_num = [1, 2, 2, 3, 8]`
2. `dic = {1: 0, 2: 1, 3: 3, 8: 4}`
3. For each num in `nums`, lookup in `dic`:

   * 8 → 4
   * 1 → 0
   * 2 → 1
   * 2 → 1
   * 3 → 3
4. `ans = [4, 0, 1, 1, 3]`

✅ Correct output.

---

### 🔄 Time & Space Complexity:

* **Time:** `O(n log n)` due to sorting
* **Space:** `O(n)` for `dic` and `ans`

---



