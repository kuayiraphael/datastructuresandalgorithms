# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_number = float("inf")
        min_row = -1
        max_number = float("-inf")
        max_row = -1

        for row in range(len(arrays)):
            if min_number > arrays[row][0]:
                min_row = row
                min_number = arrays[row][0]


        for row in range(len(arrays)):
            if max_number <arrays[row][-1] and min_row !=row:
                max_row = row
                max_number = arrays[row][-1]

        mina_number = float("inf")
        mina_row = -1
        maxa_number = float("-inf")
        maxa_row = -1

        for row in range(len(arrays)):
            if maxa_number <arrays[row][-1]:
                maxa_row = row
                maxa_number = arrays[row][-1]

        for row in range(len(arrays)):
            if mina_number > arrays[row][0] and maxa_row!=row:
                mina_row = row
                mina_number = arrays[row][0]



        return max(max_number - min_number,maxa_number-mina_number)




      