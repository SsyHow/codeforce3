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
    n = II()
    a = LII()
    b = LII()

    x = 0
    for i in a:
        x ^= i
    for i in b:
        x ^= i

    if x == 0:
        print("Tie")
        continue

    idx = 0
    for i in range(n):
        if a[i] ^ b[i]:
            idx = i
    print("Ajisai" if idx & 1 == 0 else "Mai")
