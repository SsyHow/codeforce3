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
from collections import Counter

L = LII()
c = Counter(L).most_common()

# print(c)
if c[0][1] == 6 or c[0][1] == 4 and c[1][1] == 2:
    print("Elephant")
elif c[0][1] >= 4 and c[1][1] == 1 :
    print("Bear")
else:
    print("Alien")

