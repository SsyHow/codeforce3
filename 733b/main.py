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
L = []
l = r = 0
for _ in range(a):
    x, y = MII()
    l += x
    r += y
    L.append((x, y))

num = 0
ans = abs(l - r)
for i in range(a):
    k = abs((l - L[i][0] + L[i][1]) - (r - L[i][1] + L[i][0]))
    if ans < k:
        num = i + 1
        ans = k
print(num)