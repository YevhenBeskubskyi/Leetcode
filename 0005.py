# Leetcode 0005 (Medium): Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ''
        k = lambda x: len(x)
        
        for i in range(len(s)):
            a = helper(i, i)
            b = helper(i, i+1)
            res = max(res, a, b, key=k)

        return res
