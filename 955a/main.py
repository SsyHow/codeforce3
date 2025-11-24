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
h, m = MII()
H, D, C, N = MII()
if h <= 19:
    before = (H + N - 1) // N * C
    after = (((20 - h) * 60 - m) * D + H + N - 1) // N * C * 0.8

    print(min(before, after))
else:
    print((H + N - 1) // N * C * 0.8)
