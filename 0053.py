# Leetcode 0053 (Easy): Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        cursum = float('-inf')
        for num in nums:
            cursum = max(cursum+num, num)
            maxsum = max(maxsum, cursum)
        return maxsum
