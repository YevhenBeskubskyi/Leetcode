def generate_parentheses(n):
    '''
    Leetcode 0022 (Medium): Generate Parentheses
    https://leetcode.com/problems/generate-parentheses/
    '''
    parentheses = []
    stack = []

    def backtrack(o, c):
        if o == c == n:
            s = ''.join(stack)
            parentheses.append(s)
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
    return parentheses
