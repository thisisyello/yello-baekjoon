import sys
input = sys.stdin.readline

n = int(input())
words_list = []

for _ in range(n):
    word = input().strip()
    words_list.append(word)

set_list = set(words_list)
sort_list = sorted(set_list, key=lambda word: (len(word), word))

for w in sort_list:
    print(w)