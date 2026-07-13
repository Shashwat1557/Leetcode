class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        for length in range(2, 10):
           
            for start in range(10 - length):
                num = int(digits[start:start + length])
                
                # If within range, add it to our results
                if low <= num <= high:
                    result.append(num)
                # Small optimization: if we exceed high, we can stop for this length
                elif num > high:
                    break
                    
        return result