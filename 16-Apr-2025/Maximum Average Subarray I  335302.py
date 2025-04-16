# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        left = 0
        right = k 
        max_total = total      

        while right<len(nums):
            total = total - nums[left] +nums[right]
            max_total = max(max_total,total)
            left +=1
            right +=1
        return max_total/k


        