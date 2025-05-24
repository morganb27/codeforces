import sys

# Redefine input() to read one line at a time
input = sys.stdin.readline
n = int(input())
count = 0

for _ in range(n):
    round = input().split()
    if sum(1 for num in round if num == "1") > 1:
        count+=1

print(count)