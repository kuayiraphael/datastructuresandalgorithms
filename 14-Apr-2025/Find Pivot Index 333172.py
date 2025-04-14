# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*(n+1)

        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1]+ nums[i-1]

        for j in range(n):
            if prefix_sum[j]==prefix_sum[n]-prefix_sum[j+1]:
                return j
        return -1        