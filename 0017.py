# Leetcode 0017 (Medium): Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        chars = {}
        chars['2'] = 'abc'
        chars['3'] = 'def'
        chars['4'] = 'ghi'
        chars['5'] = 'jkl'
        chars['6'] = 'mno'
        chars['7'] = 'pqrs'
        chars['8'] = 'tuv'
        chars['9'] = 'wxyz'
        
        def addChar(char, combinations):
            for i in range(len(combinations)):
                combinations[i] += char
            return combinations
        
        def addDigit(digit, combinations):
            digitCombinations = []
            digitChars = chars[digit]
            for char in digitChars:
                digitCombinations += addChar(char, combinations[:])
            return digitCombinations
        
        res = ['']
        for digit in digits:
            res = addDigit(digit, res)
        return sorted(res)
