class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        compare_nums = [i for i in range(len(nums) + 1) if i not in nums]
        return int( compare_nums[0])

        