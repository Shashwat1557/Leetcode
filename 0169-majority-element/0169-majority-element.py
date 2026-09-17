class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        m = n//2
        return nums[m]       