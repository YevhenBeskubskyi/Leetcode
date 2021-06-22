def daily_temperatures(temperatures):
    '''
    Leetcode 0739 (Medium): Daily Temperatures
    '''
    stack = []
    res = [0] * len(temperatures)
    
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            tmp, idx = stack.pop()
            res[idx] = i - idx
        stack.append([t, i])
    
    return res
