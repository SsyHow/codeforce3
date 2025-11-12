import sys

input = lambda: sys.stdin.readline().rstrip()


def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L = []
for _ in range(8):
    L.append(list(I()))
ans = 0
for i in range(8):
    if all(L[i][j] == 'B' for j in range(8)):
        ans += 1
    if all(L[j][i] == 'B' for j in range(8)):
        ans += 1
print(ans if ans < 16 else 8)