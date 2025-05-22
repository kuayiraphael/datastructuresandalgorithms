# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)[2:]
        s = str(a)
        return s.count("1")
        # return str(a).count(1)