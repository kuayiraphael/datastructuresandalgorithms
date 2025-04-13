# Problem: E - Coins - https://codeforces.com/gym/602997/problem/E

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())


    if k %2==0 and n%2==1:
        print( "NO")
    else:
        print("YES")