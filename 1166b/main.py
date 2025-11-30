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
k = II()
f = False
a = 1
for i in range(5, k//5 + 1):
    if k // i * i == k:
        f = True
        a = i
        break
if f:
    b = k//i
    ans = []
    for x in range(a):
        s = 'aeiou'[x:] + 'aeiou'[:x]
        ans.append(s * (b // 5) + s[:b%5])
    # print(ans)
    print(''.join(ans))

else:
    print(-1)
