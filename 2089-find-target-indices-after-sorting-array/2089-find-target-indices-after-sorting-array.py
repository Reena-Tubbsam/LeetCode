class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arry = []
        if target not in nums:
            return arry
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                arry.append(i)
        return arry
        