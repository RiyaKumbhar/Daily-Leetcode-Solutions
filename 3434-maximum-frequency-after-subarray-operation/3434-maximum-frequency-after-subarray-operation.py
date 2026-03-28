from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count_k = nums.count(k)
        max_gain = 0

        for target in set(nums):
            if target == k:
                continue
            
            curr = 0
            best = 0

            for num in nums:
                if num == target:
                    curr += 1
                elif num == k:
                    curr -= 1
                
                curr = max(curr, 0)
                best = max(best, curr)
            
            max_gain = max(max_gain, best)

        return count_k + max_gain