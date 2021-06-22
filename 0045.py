def jump(nums):
    '''
    Leetcode 45 (Medium): Jump Game II 
    '''
    jumps = [i for i in range(len(nums))]
    for i in range(len(jumps)):
        for j in range(i+1, min(len(jumps), nums[i]+i+1)):
            jumps[j] = min(jumps[j], jumps[i]+1)
    return jumps[-1]
