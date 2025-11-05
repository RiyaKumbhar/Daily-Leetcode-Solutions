class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        first_max = max(nums)
        unique_nums -= set([first_max])
        try:
            sec_max = max(list(unique_nums))
            unique_nums -= set([sec_max])
            return max(list(unique_nums))
        except:
            return first_max