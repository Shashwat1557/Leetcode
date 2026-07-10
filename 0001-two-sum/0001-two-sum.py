class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num  # Find the required complement
            if complement in num_map:
                return [num_map[complement], i]  # Return indices
            num_map[num] = i  # Store the current number with its index
        return []  # This line will never execute as per constraints