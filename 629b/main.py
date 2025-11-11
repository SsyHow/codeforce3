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
n = II()
M = []
F = []
for i in range(n):
    s, x, y = LI()
    x = int(x)
    y = int(y)
    if s == 'M':
        M.append((x, y))
    else:
        F.append((x, y))
ans = 0
for i in range(1, 367):
    males = 0
    fems = 0
    for x, y in M:
        if x <= i <= y:
            males += 1
    for x, y in F:
        if x <= i <= y:
            fems += 1

    ans = max(ans, min(males, fems))
print(ans * 2)
