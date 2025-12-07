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

def check(x, d):
    while x:
        if x % 10 == d:
            return True
        x //= 10
    return False

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    q, d = MII()
    L = LII()

    for i in L:
        if i >= d * 10:
            print("YES")
            continue

        while i > 0 and not check(i, d):
            i -= d

        if i > 0 :
            print("YES")
        else:
            print("NO")

