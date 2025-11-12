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
L = []
for _ in range(a):
    x, y = MII()
    L.append((x, y))

if a == 3 or a == 4:
    L.sort()
    x, y = L[0]
    i = 1
    while i < a:
        if L[i][0] != x and L[i][1] != y:
            m, n = L[i][0], L[i][1]
            break
        i += 1
    else:
        x, y = L[1][0], L[1][1]
        m, n = L[2][0], L[2][1]
    print(abs(x - m) * abs(y - n))
elif a == 1:
    print(-1)

else:
    if L[0][0] != L[1][0] and L[0][1] != L[1][1]:
        print(abs(L[1][0] - L[0][0]) * abs(L[1][1] - L[0][1]))
    else:
        print(-1)