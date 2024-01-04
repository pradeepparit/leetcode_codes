from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        count = 0
        for value in freq.values():
            if value == 1:
                return -1
            count += (value // 3)
            if value % 3 == 2 or value % 3 == 1:
                count += 1
        
        return count
