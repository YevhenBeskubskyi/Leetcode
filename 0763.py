# Leetcode 0763 (Medium): Partition Labels
# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {c:i for i, c in enumerate(s)}
        res, maxind, size = [], -1, 1
        
        for i, c in enumerate(s):
            maxind = max(maxind, last[c])
            if i == maxind:
                res.append(size)
                size = 1
            else:
                size += 1
                
        return res
