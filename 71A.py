import sys

# Redefine input() to read one line at a time
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    word = input().strip()
    if len(word) <= 10:
        print(word)
    else:
        first_letter = word[0]
        last_letter = word[-1]
        in_between_count = len(word) - 2
        print(first_letter + str(in_between_count) + last_letter)