"""
Maximum Product Subarray --> Medium

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# Brute Force Code (O(n²))
# ✔ Time complexity: O(n²)
# ✔ Space complexity: O(1)

def maxProduct(nums):
    n = len(nums)
    ans = float('-inf')

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            ans = max(ans, prod)

    return ans

#
# if __name__ == '__main__':
#     # Example 1
#     nums1 = [2, 3, -2, 4]
#     print(maxProduct(nums1))  # Output: 6
#
#     # Example 2
#     nums2 = [-2, 0, -1]
#     print(maxProduct(nums2))  # Output: 0
#
#     # Additional Test Cases
#     nums3 = [-2, 3 , -4]
#     print(maxProduct(nums3))  # Output: 24


"""
# Kadane's Algorithm Adaptation (O(n) time | O(1) space)
"""

def maxProduct(nums):
    max_prod = min_prod = ans = nums[0]

    for n in nums[:]:
        if n < 0:
            n = -n
            # max_prod, min_prod = min_prod, max_prod  # swap when negative

        max_prod = max(n, max_prod * n)
        # min_prod = min(n, min_prod * n)

        ans = max(ans, max_prod)

    return ans


if __name__ == '__main__':
    # Example 1
    nums1 = [2, 3, -2, 4]
    print(maxProduct(nums1))  # Output: 6
    #
    # # Example 2
    # nums2 = [-2, 0, -1]
    # print(maxProduct(nums2))  # Output: 0

    # Additional Test Cases
    nums3 = [-2, 3 , -4]
    print(maxProduct(nums3))  # Output: 24