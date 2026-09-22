class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        num_ones = 0
        best = 0

        for i in nums:
            if i == 1:
                num_ones = num_ones + 1
                if num_ones > best:
                    best = num_ones
            else:
                num_ones = 0
        return best