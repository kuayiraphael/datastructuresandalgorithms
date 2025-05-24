# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # We can make all elements equal in 3 or fewer moves

        nums.sort()
        
        # Try all 4 scenarios
        return min(
            nums[-1 - 3] - nums[0],     # Remove 3 largest
            nums[-1] - nums[0 + 3],     # Remove 3 smallest
            nums[-1 - 2] - nums[0 + 1], # Remove 2 largest, 1 smallest
            nums[-1 - 1] - nums[0 + 2], # Remove 1 largest, 2 smallest
        )
