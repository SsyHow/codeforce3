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
def check(n):

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = II()
for _ in range(a):
    m, n = MII()
    print("YES" if check((m + n)) and m - n == 1 else "NO")