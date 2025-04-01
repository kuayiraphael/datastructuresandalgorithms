# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        res=[]

        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)

        for i in range(n//2):
            res.append(pos[i])
            res.append(neg[i])
        return res


        
        