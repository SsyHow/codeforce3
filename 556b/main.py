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
L = LII()

k = L[0]

for i in range(a):
    # print(L[i] - k * (-1) ** i)
    if i == (L[i] - k * (-1) ** i) % a:
        continue
    else:
        print("NO")
        break
else:
    print("YES")
