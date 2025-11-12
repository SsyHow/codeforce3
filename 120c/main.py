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
with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    L = list(map(int, f.readline().split()))

    ans = 0
    for i in L:
        if i >= 3 * k:
            ans += i - 3 * k
        else:
            ans += i % k
with open('output.txt', 'w') as x:
    print(ans, file = x)