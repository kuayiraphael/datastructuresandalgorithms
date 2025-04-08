# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        pivot = max(arr)
        pivot_index = -1


        if n<3:
            return False
        for i in range(n):
            if arr[i]==pivot:
                pivot_index = i
                break
        print(pivot_index)

        if pivot_index==len(arr)-1 or pivot_index==0:
            return False

        def first_half_check(arr):
            for i in range(1,len(arr)):
                if arr[i-1] >= arr[i]:
                    return False 
            return True
        
        def second_half_check(arr):
            for i in range(1,len(arr)):
                if arr[i-1] <= arr[i]:
                    return False 
            return True

        
        if first_half_check(arr[:pivot_index]) and second_half_check(arr[pivot_index:]):
            return True 
        return False

            
