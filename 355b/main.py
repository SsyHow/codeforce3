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
c1, c2, c3, c4 = MII()

n, m = MII()
L = LII()
M = LII()

k1 = 0
for i in L:
    k1 += min(i * c1, c2)
k1 = min(k1, c3)

k2 = 0
for i in M:
    k2 += min(i * c1, c2)
k2 = min(k2, c3)
print(min(k1 + k2, c4))