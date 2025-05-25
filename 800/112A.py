import sys

# Redefine input() to read one line at a time
input = sys.stdin.readline
first = input()
second = input()

for a, b in zip(first, second):
    a, b = a.lower(), b.lower()
    if ord(a) < ord(b):
        print("-1")
        break
    if ord(a) > ord(b):
        print("1")
        break
else:
    print("0")

