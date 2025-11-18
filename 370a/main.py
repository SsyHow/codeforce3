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
r1, c1, r2, c2 = MII()
rook = 1 if r1 == r2 or c1 == c2 else 2
bishop = 0
if (r1 - c1) % 2 == (r2 - c2) % 2:
    bishop = 1 if abs(r2 - r1) == abs(c2 - c1) else 2
king = max(abs(r1 - r2), abs(c1 - c2))
print(rook, bishop, king)