class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        middleElement = nums[len(nums)//2]
        return middleElement
