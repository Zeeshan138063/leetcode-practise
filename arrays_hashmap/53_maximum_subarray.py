# https://leetcode.com/problems/maximum-subarray/
# https://docs.google.com/spreadsheets/d/1Mf_oXUkabgIF1mBH2sNiRKR4rh3uE7LCoQTvdLYMmXU/edit?usp=sharing
"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

"""
✅ Brute Force Code (O(n²))
Idea:

Check every possible subarray, calculate its sum, and keep the maximum.
Since a subarray is defined by:
A start index i
An end index j (≥ i)

Time complexity:
Outer loop: O(n)
Inner loop: O(n)
Total: O(n²)
Space: O(1)

"""

# name this function as per the python standard naming convention
def max_sub_array_brute_force(nums):

    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]  # sum of subarray nums[i:j+1]
            max_sum = max(max_sum, current_sum)

    return max_sum


"""
✅ Problem: Maximum Subarray
 https://leetcode.com/problems/maximum-subarray/description/

 Solution 2: Optimal Code  O(n) time | O(1) space
 (Kadane’s Algorithm)
🎯 Intuition (Before Coding)

Think like this:
As you walk through the array, at each position you have two choices:
Extend the existing subarray (add current number)
Start a new subarray from the current number
Which is better?
→ Choose the one that gives a bigger sum.

"""


def max_sub_array_kadane_algo(nums):
    current_max = global_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(global_max, current_max)
    return global_max