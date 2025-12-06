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
    s = list(I())
    b = II()
    n = len(s)
    cnt = 0
    for i in range(n):
        if ''.join(s[i:i + 4]) == '1100':
            cnt += 1

    for _ in range(b):
        i, v = MII()
        i -= 1
        curr = ''.join(s[max(0, i - 3):i + 4]).count('1100')
        s[i] = str(v)
        conn = ''.join(s[max(0, i - 3):i + 4]).count('1100')
        cnt += conn - curr
        print("Yes" if cnt > 0 else "No")


