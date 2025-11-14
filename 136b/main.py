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

L = []
while a or b:
    # print(a%3, b%3)
    L.append((b%3 - a%3 + 3)%3)
    a //= 3
    b //= 3

# print(L)
ans = 0
while L:
    ans = 3 * ans + L.pop()
print(ans)
