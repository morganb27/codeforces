import sys
from collections import defaultdict

# Redefine input() to read one line at a time
input = sys.stdin.readline
n = int(input())
res = defaultdict(int)

for _ in range(n):
    team = input().strip()
    res[team] += 1
    
print(max(res, key = res.get))
    
    

