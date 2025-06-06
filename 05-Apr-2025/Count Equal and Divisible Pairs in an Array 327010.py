# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
            
        return count