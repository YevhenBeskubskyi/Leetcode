# Leetcode 0198 (Medium): House Robber
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        tab = [0] * len(nums)
        tab[0] = nums[0]
        if len(nums) > 1: tab[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            tab[i] = max(tab[i-2] + nums[i], tab[i-1])
        
        return tab[-1]
    
