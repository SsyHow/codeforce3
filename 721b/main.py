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
n, k = MII()
dic = {}
for _ in range(n):
    s = I()
    dic[len(s)] = dic.get(len(s), 0) + 1

s = I()

x = len(s)
# print(dic)
cnt1 = 1
cnt2 = 0
for i in dic:
    if i < x:
        cnt1 += dic[i]
        cnt2 += dic[i]
    elif i == x:
        cnt2 += dic[i]

print((cnt1 - 1) // k * 5 + cnt1, (cnt2 - 1) // k * 5 + cnt2)
