# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [1]*(right+1)
        prime[0]=0
        prime[1]=0
        results = [-1,-1]
        min_diff = float("inf")


        for i in range(2,int(right**(0.5))+1):
            if prime[i]:
                start = i*i
                end = right +1
                while start<end:
                    prime[start] = 0
                    start +=i

        array = [i for i in range(left,right+1) if prime[i]]


        if len(array)<2:
            return results
            
        for i in range(len(array)-1):
            diff = array[i+1]-array[i]

            if diff<min_diff:
                min_diff = diff
                results = [array[i],array[i+1]]

        return results


