def two_sum(nums, target):
    '''
    Leetcode 0001 (Easy): Two Sum
    '''
    diff = dict()
    
    for i, num in enumerate(nums):
        if num in diff:
            return [diff[num], i]
        diff[target-num] = i
    
    return [-1, -1]
