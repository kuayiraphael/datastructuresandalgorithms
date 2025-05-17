# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count_nums =  [0]*3
        res = []


        for i in range(len(nums)):
            count_nums[nums[i]]+=1


        for i in range(len(count_nums)):
            for j in range(count_nums[i]):
                res.append(i)    
        
        for i in range(len(nums)):
            nums[i]=res[i]
