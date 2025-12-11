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

def get(L, k):
    mx1, mx2, mx3 = -1, -1, -1
    for i in range(k):
        if mx1 == -1 or L[i] > L[mx1]:
            mx3 = mx2
            mx2 = mx1
            mx1 = i
        elif mx2 == -1 or L[i] > L[mx2]:
            mx3 = mx2
            mx2 = i
        elif mx3 == -1 or L[i] > L[mx3]:
            mx3 = i
    return mx1, mx2, mx3

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    x = II()
    a = LII()
    b = LII()
    c = LII()

    ans = 0
    for i in get(a, x):
        for j in get(b, x):
            for k in get(c, x):
                if i != j and i != k and j != k:
                    ans = max(ans, a[i] + b[j] + c[k])
    print(ans)