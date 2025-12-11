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
L = LII()

cnt = 0
for i in L:
    if i == 0 and cnt == 1:
        print("NO")
        break
    if i & 1 and cnt == 1:
        cnt = 0
    elif i & 1 and cnt == 0:
        cnt = 1
    elif i & 1 == 0 and cnt == 1:
        cnt = 1
    else:
        cnt = 0
else:
    print("NO" if cnt else "YES")