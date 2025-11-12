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
L = LII()
n = II()
dic = {
    'S': [0, 1, 2, 3, 4],
    'M': [0, 1, -1, 2, 3],
    'L': [0, 1, -1, 2, -2],
    'XL': [0, 1, -1, -2, -3],
    'XXL': [0, -1, -2, -3, -4]
}
x = {
    'S': 0,
    'M': 1,
    'L': 2,
    'XL': 3,
    'XXL': 4
}
y = {v:k for k, v in x.items()}
for _ in range(n):
    s = I()
    i = 0
    while L[x[s] + dic[s][i]] == 0:
        i += 1
    L[x[s] + dic[s][i]] -= 1
    print(y[x[s] + dic[s][i]])

