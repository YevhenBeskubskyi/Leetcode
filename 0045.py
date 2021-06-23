# Leetcode 45 (Medium): Jump Game II 
# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float('inf') for _ in range(len(nums))]
        steps[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                steps[j] = min(steps[j], steps[i] + 1)
        return steps[-1]
