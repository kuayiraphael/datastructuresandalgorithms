# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        n = len(friends)


        start_index = 0

        while n > 1:
            removal_index = (start_index + k-1)%n

            friends.pop(removal_index)

            start_index = removal_index
            n = n -1

        return friends[0]    
