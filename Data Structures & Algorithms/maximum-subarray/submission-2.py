class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSub = nums[0], 0

        for n in nums:
            curSub = max(curSub, 0) + n
            maxSub = max(maxSub, curSub)
        return maxSub