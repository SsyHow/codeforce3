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
t = II()
for _ in range(t):
    a = II()
    s = I()

    if s[-1] == '1' or s[0] == '1':
        print("YES")
        continue
    for i in range(1, a - 1):
        if s[i] == '0' or (s[i] == '1' and s[i - 1] == '0' and s[i + 1] == '0'):
            continue
        else:
            print("YES")
            break
    else:
        print("NO")

