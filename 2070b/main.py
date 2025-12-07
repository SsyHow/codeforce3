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
    n, start, k = MII()
    s = I()
    loop = 0
    x = 0
    for i in s:
        if i == 'L':
            x -= 1
        else:
            x += 1
        loop += 1
        if x == 0:
            break
    else:
        loop = 1 << 60
    i = 0
    ans = 0
    while i < n and i < k:
        if s[i] == 'L':
            start -= 1
        else:
            start += 1

        if start == 0:
            ans += 1
            break
        i += 1
    if start != 0:
        print(ans)
        continue
    if k - i - 1 > 0:
        ans += (k - i - 1) // loop

    print(ans)
