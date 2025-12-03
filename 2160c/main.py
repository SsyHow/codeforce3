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
    b = II()
    # print(b & -b)
    if b == 0:
        print("YES")
        continue

    b //= b & -b
    k = bin(b)[2:]
    if k == k[::-1] and (len(k) & 1 == 0 or k[len(k)//2] == '0'):
        print("YES")
    else:
        print("NO")
