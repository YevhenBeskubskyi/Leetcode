# Leetcode 0001 (Easy): Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                return i, d[nums[i]]
            d[target-nums[i]] = i
        return [-1, -1]
