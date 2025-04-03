# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        countNums = {}
        result = []

        for i in nums:
            if i in countNums:
                countNums[i]+=1
            else:
                countNums[i]=1

        for i,k in countNums.items():
            if k==2:
                result.append(i)
        return result   
        