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

    L = []
    for i in range(b):
        tmp = []
        for j in range(b):
            tmp.append((i * b) + (j + 1))
        L.append(tmp)
    ans = 0

    for i in range(b):
        for j in range(b):
            tmp = L[i][j]

            if i > 0:
                tmp += L[i - 1][j]
            if i < b - 1:
                tmp += L[i + 1][j]
            if j > 0:
                tmp += L[i][j - 1]
            if j < b - 1:
                tmp += L[i][j + 1]

            ans = max(tmp, ans)
    print(ans)


