# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

w = int(input())


def check(w):
    if w == 2:
        return "NO"
    if w % 2 == 0:
        return "YES"
    return "NO"

print(check(w))
