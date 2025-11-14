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
a = II()

L = LII()
L.sort()
ans = 1 << 60
cnt = 0
for i in range(a - 1):
    if L[i + 1] - L[i] < ans:
        cnt = 1
        ans = L[i + 1] - L[i]
    elif L[i + 1] - L[i] == ans:
        cnt += 1
print(ans, cnt)

