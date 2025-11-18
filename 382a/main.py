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
L = I().split('|')
s = I()
a = len(s)
L[0] = list(L[0])
L[1] = list(L[1])
i = 0

while i < a:
    if len(L[0]) <= len(L[1]):
        L[0].append(s[i])
    else:
        L[1].append(s[i])
    i += 1
print(''.join(L[0]) + '|' + ''.join(L[1]) if len(L[0]) == len(L[1]) else "Impossible")