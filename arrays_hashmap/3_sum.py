# https://leetcode.com/problems/3sum/
from typing import List


def threeSum( nums: List[int]) -> List[List[int]]:
    if min(nums) > 0: 
            return []
        
    nums = sorted(nums)    # sort the array to make it easier to find the triplets
    # Sorting:        O(n log n)

    n = len(nums)
    ans = []
    # For i loop: runs n times
    for i in range(n-2):
        
         if nums[i] > 0: 
                break

         # optimization step
         if i > 0 and nums[i]== nums[i-1]:
             continue

         left = i + 1
         right = n - 1
         # For two-pointer movement: at most n per i
         while left < right:

             curr_sum = nums[i] + nums[left] + nums[right]
             if curr_sum > 0:
                 right = right - 1
             elif curr_sum < 0:
                 left = left + 1
             else:
                 ans.append((nums[i], nums[left], nums[right]))
                 left += 1
                 right -= 1
                 while left < right and nums[left] == nums[left-1]:
                     left += 1
                 while left < right and nums[right] == nums[right+1]:
                    right -= 1

    return ans

# Total: O(n * n) = O(n²)

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]s
    nums = [0,0,0]
    print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]s
