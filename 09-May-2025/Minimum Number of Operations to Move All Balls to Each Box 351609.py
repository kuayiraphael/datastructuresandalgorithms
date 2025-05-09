# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        count = 0
        steps = 0
        for i in range(n):
            # print(steps)
            res[i] += steps
            if boxes[i] == '1':
                count += 1
            steps += count

        count = 0
        steps = 0
        for i in range(n - 1, -1, -1):
            res[i] += steps
            if boxes[i] == '1':
                count += 1
            steps += count

        return res

