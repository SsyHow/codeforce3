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
def dfs(i, m):
    if i == x:
        return m
    return max(dfs(i + 1, m - a[i]), dfs(i + 1, b[i] - m))
t = II()
for _ in range(t):
    x = II()
    a = LII()
    b = LII()

    mx = mn = 0
    for i in range(x):
        nmn = min(mn - a[i], b[i] - mx)
        nmx = max(mx - a[i], b[i] - mn)
        mn, mx = nmn, nmx
    print(mx)