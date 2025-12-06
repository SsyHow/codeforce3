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
    L = LII()

    idx1 = idx2 = idxn = 0
    for idx, i in enumerate(L):
        if i == 1:
            idx1 = idx + 1
        if i == 2:
            idx2 = idx + 1
        if i == b:
            idxn = idx + 1

    if idx1 < idxn < idx2 or idx1 > idxn > idx2:
        print(idxn, idxn)

    elif idxn > idx1 and idxn > idx2:
        print(idxn, max(idx1, idx2))
    else:
        print(idxn, min(idx1, idx2))
