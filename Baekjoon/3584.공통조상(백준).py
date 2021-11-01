"""
트리, 그래프탐색
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[b] = a

    s1, s2 = map(int, input().split())
    parent1 = [s1]
    parent2 = [s2]
    while tree[s1]:
        parent1.append(tree[s1])
        s1 = tree[s1]

    while tree[s2]:
        parent2.append(tree[s2])
        s2 = tree[s2]

    i = len(parent1) - 1
    j = len(parent2) - 1

    while parent1[i] == parent2[j]:
        i -= 1
        j -= 1

    print(parent1[i+1])