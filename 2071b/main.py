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

s = [1, 8, 49, 288, 1681, 9800, 57121, 332928]

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()


    if b in s:
        print(-1)
    else:
        L = list(range(1, b + 1))
        i = 0
        while i < 8 and s[i] < b:
            L[s[i] - 1], L[s[i]] = L[s[i]], L[s[i] - 1]
            i += 1
        print(*L)



