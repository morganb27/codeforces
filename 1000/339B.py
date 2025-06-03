import sys
from collections import defaultdict

# Redefine input() to read one line at a time
input = sys.stdin.readline
num_houses, num_tasks = map(int, input().split())
tasks = list(map(int, input().split()))

current = 1
distance = 0


for task in tasks:
    if current <= task:
        distance += task - current
    else:
        distance += num_houses + (task - current)
    current = task

print(distance)
        
    