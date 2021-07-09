# Leetcode 0416 (Medium): Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2): return False
        target = sum(nums) // 2
        
        dp = set()
        dp.add(0)
        
        for num in nums:
            newDp = set()
            for t in dp:
                newDp.add(t + num)
                newDp.add(t)
            dp = newDp
        
        return target in dp
