# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def Check(nums):
            return nums[0] + nums[1] > nums[2] and nums[1] + nums[0] > nums[2] and nums[0] + nums[2] >nums[1]

        nums.sort()

        if len(nums)==3 and Check(nums):
            return sum(nums)

        max_area = 0
        print(nums)

        for i in range(len(nums)-2):
            if Check(nums[i:i+3]):
                max_area = max(max_area,sum(nums[i:i+3]))
        return max_area
        