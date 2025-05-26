import sys

# Redefine input() to read one line at a time
input = sys.stdin.readline
str = input().strip()
vowels = ["a", "e", "i", "o", "u", "y"]
res = ""

for char in str:
    if char.lower() not in vowels:
        res += "." + char.lower()

print(res)