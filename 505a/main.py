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

def check(k):
    return k == k[::-1]


# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = I()
t = set(list(s))
f = False
for i in range(0, len(s) + 1):
    for j in s:
        k = s[:i] + j + s[i:]
        if check(k):
            print(k)
            f = True
            break
    if f:
        break
else:
    print("NA")
