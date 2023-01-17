"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

print("Two Sum Solutions 👨‍💻")

nums = [2, 7, 11, 15]
target = 9
print(nums)
class Solution:
    # O(n^2)
    def exp_time(self, nums: list, target: int):
        for i in nums:
            for j in nums:
                if (i+j) == target:
                    return [nums.index(i), nums.index(j)]
    # O(n)
    def optimal_solution(self, nums: list, target: int):
        # Create an empty Hash-Map / Dictionary
        hashMap = {}
        # Iterate through the list of number (array of numbers)
        for i, n in enumerate(nums):
            # Check if the complement of the current number (target minus n) exist in the Dictionary
            if (target - n) in hashMap:
                # If complement exisit in Dictionary return indices
                return hashMap[ans], i
            # If complement is not found add current number and its index to the Dictionary
            hashMap[n] = i
        # If sum of two numbers in the list do no equal the target return an empty list
        return []

s = Solution()
print(s.exp_time(nums, target))
print(s.optimal_solution(nums, target))

"""
This solution has a time complexity of O(n) because
we are iterating through the list of nums once
and performing constant time dictionary operations for each number.
Iterating through the list of numbers
and for each number in the list check if the complement (target - num)
is already contained in the Dictionary.
If it is, then the two numbers that add up to the target have been found
and their indices are returned.
If not, add the current number and
its index to the dictionary and move on to the next number.
"""
