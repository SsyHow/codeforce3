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
a1, b1 = MII()
a2, b2 = MII()
a3, b3 = MII()

z = a3
y = a2
k = a - z - y
if k == a1:
    x = a1
    print(x, y, z)
else:
    x = min(k, b1)
    y = min(a - x - z, b2)
    z = a - x - y
    print(x, y, z)