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
t = II()
for _ in range(t):
    n, s = MII()
    L = LII()

    ss = sum(L)

    if ss > s:
        print(*L)

    elif ss == s:
        print(-1)
    else:
        if s - ss == 1:
            k = '0' * L.count(0) + '2' * L.count(2) + '1' * L.count(1)
            print(*k, sep = ' ')
        else:
            print(-1)