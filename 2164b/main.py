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

def solve():
    b = II()
    L = LII()

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if (L[j] % L[i]) & 1 == 0:
                print(L[i], L[j])
                return

    print(-1)
a = II()
for _ in range(a):
    solve()