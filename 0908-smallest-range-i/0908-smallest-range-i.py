class Solution(object):
    def smallestRangeI(self, nums, k):
        if not nums: 
            return 0
        originoal_max = max(nums)
        original_min = min(nums)
        diff = max(nums)-min(nums)
        return max(0, diff - 2 * k)
        