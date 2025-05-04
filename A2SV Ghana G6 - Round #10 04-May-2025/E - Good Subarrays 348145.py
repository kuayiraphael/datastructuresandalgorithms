# Problem: E - Good Subarrays - https://codeforces.com/gym/607807/problem/E

def Check(a,n):
    Dict = {0:1}
    running_sum = 0
    count = 0
 
    for i in range(len(a)):
        running_sum += a[i]-1 
        count += Dict.get(running_sum,0)
        Dict[running_sum] = Dict.get(running_sum,0)+1
 
    return count
  
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(input())
    a = [ int(i) for i in a]
    # print(a)
    print(Check(a,n))