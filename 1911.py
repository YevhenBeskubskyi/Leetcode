# Leetcode 1911 (Medium): Maximum Alternating Subsequence Sum
# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        evensum, oddsum = 0, 0
        for i in range(len(nums) -1, -1, -1):
            tmpeven = max(oddsum + nums[i], evensum)
            tmpodd = max(evensum - nums[i], oddsum)
            evensum, oddsum = tmpeven, tmpodd
        return evensum

# class Solution:
#     def maxAlternatingSum(self, nums: List[int]) -> int:
#         tab = {}
        
#         def dfs(i, even):
#             if i == len(nums):
#                 return 0
#             if (i, even) in tab:
#                 return tab[(i, even)]
            
#             total = nums[i] if even else -nums[i]
#             x = total + dfs(i + 1, not even)
#             y = dfs(i + 1, even)
#             tab[(i, even)] = max(x, y)
            
#             return tab[(i, even)]
        
#         return dfs(0, True)
