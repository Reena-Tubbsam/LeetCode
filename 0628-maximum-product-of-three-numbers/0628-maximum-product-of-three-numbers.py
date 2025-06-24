class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
         # Option 1: top three
        max1 = nums[-1]*nums[-2]*nums[-3]
         # Option 2: two smallest (negatives) and the largest
        max2 = nums[0]*nums[1]*nums[-1]
        return max(max1,max2)
        