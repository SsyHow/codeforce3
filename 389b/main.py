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
    L.append(list(I()))

for i in range(1, a - 1):
    for j in range(1, a - 1):
        if L[i][j] == '#' and L[i - 1][j] == '#' and L[i  + 1][j] == '#' and L[i][j - 1] == '#' and L[i][j + 1] == '#':
            L[i][j] = '.'
            L[i - 1][j] = '.'
            L[i + 1][j] = '.'
            L[i][j - 1] = '.'
            L[i][j + 1] = '.'

def check():
    for i in range(a):
        for j in range(a):
            if L[i][j] == '#':
                return "NO"
    return "YES"
print(check())