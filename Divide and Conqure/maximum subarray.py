class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma,cu=float('-inf'),0
        for n in nums:
            cu=max(cu+n,n)
            ma=max(ma,cu)
        return ma
