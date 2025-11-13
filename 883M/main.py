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
a, b = MII()
x, y = MII()
if a == x:
    a -= 1
    x += 1
elif a < x:
    x += 1
else:
    x -= 1
if b == y:
    b -= 1
    y += 1
elif b < y:
    y += 1
else:
    y -= 1

print((abs(a - x) + abs(b - y))*2)