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
n, m = MII()
L = LII()
M = LII()

i = j = 0
l = L[i]
r = M[j]

ans = 0
while i < n and j < m:
    if l == r:
        ans += 1
        i += 1
        j += 1
        if i == n and j == m:
            break
        l = L[i]
        r = M[j]

    elif l > r:
        j += 1
        r += M[j]

    else:
        i += 1
        l += L[i]

print(ans)