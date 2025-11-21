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
    n, alice = MII()
    L = LII()

    less = more = 0
    k = 0
    for i in L:
        if i == alice:
            k += i
        elif i < alice:
            less += 1
        else:
            more += 1
    # print(less, more)
    print(alice - 1 if less > more else alice + 1)