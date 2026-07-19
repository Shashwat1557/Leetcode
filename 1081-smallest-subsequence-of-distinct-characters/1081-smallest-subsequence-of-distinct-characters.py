class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Find the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # If we already have this character in our subsequence, skip it
            if char in seen:
                continue
                
            # Maintain the monotonic nature of the stack
            # Pop characters if they are larger than the current char and appear later
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to both our stack and tracking set
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)