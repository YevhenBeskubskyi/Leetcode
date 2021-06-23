# Leetcode 0003 (Medium): Longest Substring Without Repeating Character
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        maxlen = 0
        
        i, j = 0, 0
        while j < len(s):
            letter = s[j]
            while letter in letters:
                letters.remove(s[i])
                i += 1
            letters.add(letter)
            maxlen = max(len(letters), maxlen)
            j += 1
            
        return max(len(letters), maxlen)
