# Problem: Sasha and Array Coloring - https://codeforces.com/gym/458599/problem/A


def func(n,a):
    max_sum = 0

    a.sort()

    left = 0
    right = n-1
    while left<right:
        max_sum += a[right]-a[left]
        left +=1
        right -=1
    return max_sum


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(func(n,a))