class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        char = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left +=1
            char.add(s[right]) 
            max_length = max(max_length,right-left+1)   
        return max_length