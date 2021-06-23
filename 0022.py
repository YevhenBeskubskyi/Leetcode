# Leetcode 0022 (Medium): Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        
        def backtrack(o, c):
            if o == c == n:
                result.append(''.join(stack))
                return
            
            if o < n:
                stack.append('(')
                backtrack(o+1, c)
                stack.pop()
                
            if c < o:
                stack.append(')')
                backtrack(o, c+1)
                stack.pop()
                
        backtrack(0, 0)
                
        return result
