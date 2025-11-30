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
n, m, sx, sy = MII()

for i in range(1, n + 1):
    if i & 1 == 1:
        for j in range(1, m + 1):
            print((i + sx - 2) % n + 1, (j + sy - 2) % m + 1)
    else:
        for j in range(m, 0, -1):
            print((i + sx - 2) % n + 1, (j + sy - 2) % m + 1)
