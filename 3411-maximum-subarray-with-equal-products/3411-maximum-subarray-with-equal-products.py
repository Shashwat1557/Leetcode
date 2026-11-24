import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 2  # Any subarray of length 2 is always product equivalent
        
        # Max possible LCM for values <= 10 is lcm(1..10) = 2520.
        # Max possible GCD is 10, so lcm * gcd <= 25200.
        MAX_LIMIT = 25200 

        for i in range(n):
            curr_prod = nums[i]
            curr_gcd = nums[i]
            curr_lcm = nums[i]
            
            for j in range(i + 1, n):
                curr_prod *= nums[j]
                if curr_prod > MAX_LIMIT:
                    break
                
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])
                
                if curr_prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len