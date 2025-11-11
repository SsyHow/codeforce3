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
n, k = MII()
x = n
f = 0
t = 0
while n % 5 == 0:
    f += 1
    n //= 5
while n % 2 == 0:
    t += 1
    n //= 2

# print(f, t)
print(5 **(max(0, k - f)) * 2 ** (max(0, k - t)) * x)