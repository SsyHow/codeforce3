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
    L = LII()

    if L[0] == -1 and L[-1] > -1:
        L[0] = L[-1]
    elif L[0] > - 1 and L[-1] == -1:
        L[-1] = L[0]
    elif L[0] == -1 and L[-1] == -1:
        L[0] = 0
        L[-1] = 0

    for i in range(b):
        if L[i] == -1:
            L[i] = 0
    print(abs(L[0] - L[-1]))
    print(*L)
