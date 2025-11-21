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
for _ in range(a):
    b = II()
    L = [1 << 60] + LII()
    if b & 1 == 0:
        L.append(0)
    else:
        L.append(1 << 60)
    x = L[1]
    for i in range(2, b + 1, 2):
        L[i] = max(L[i - 1], x, L[i])
        x = max(x, L[i])
    # print(L)
    ans = 0
    for i in range(1, b+1, 2):
        ans += max(L[i] - min(L[i - 1], L[i + 1]) + 1, 0)

    print(ans)