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
def f(x):
    ans = []
    f = 1
    for i in x:
        ans.append(i * f)
        f *= -1
    return ans

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n, m = MII()
L = []
for i in range(n):
    s = I()
    tmp = [i + 1]
    for j in range(m):
        tmp.append(ord(s[j]) - ord('A'))
    L.append(tmp)

L.sort(key = lambda x: f(x[1:]))
print(*(i[0] for i in L))