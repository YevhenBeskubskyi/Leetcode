# Leetcode 0005 (Medium): Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result = max(s[l:r+1], result, key=lambda x : len(x))
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result = max(s[l:r+1], result, key=lambda x : len(x))
                l -= 1
                r += 1
                
        return result
