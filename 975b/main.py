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
a = LII()


def score(i):
    b = a[i + 1:] + a[0:i] + [0]
    for j in range(14):
        b[j] += a[i] // 14
    for j in range(a[i] % 14):
        b[j] += 1
    return sum(x for x in b if x % 2 == 0)


print(max(score(i) for i in range(14)))