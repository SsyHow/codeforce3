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
    s = I()
    L = []
    ans = 0
    if s[0] > s[-1]:
        for idx, i in enumerate(s):
            if s[0] >= i >= s[-1]:
                L.append((idx + 1, ord(i)))
        L.sort(key = lambda x: (-x[1], x[0]))
        ans = 0
        for i in range(len(L) -1):
            ans += abs(L[i + 1][1] - L[i][1])
    else:
        for idx, i in enumerate(s):
            if s[0] <= i <= s[-1]:
                L.append((idx + 1, ord(i)))
        L.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        for i in range(len(L) - 1):
            ans += abs(L[i + 1][1] - L[i][1])
    print(ans, len(L))
    print(*[i[0] for i in L])
