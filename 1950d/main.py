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

# def ok(n):
#     if n == 1:
#         return True
#     ans = False
#     for i in bd:
#         if n % i == 0:
#             ans |= ok(n/i)
#
#     return ans
#
# def solve():
#     n = II()
#     print("Yes" if ok(n) else "No")
#
# bd = []
# for i in range(2, 100007):
#     curr = i
#     bad = False
#     while curr:
#         if curr % 10 > 1:
#             bad = True
#             break
#         curr //= 10
#     if not bad:
#         bd.append(i)
# t = II()
# for i in range(t):
#     solve()

binary = []
for i in range(1, 32):
    x = int(f'{i:b}')
    binary.append(x)

t = II()
for _ in range(t):
    n = II()
    for i in binary:
        while n % i == 0:
            n //= i

    if n == 1:
        print("YES")
    else:
        print("NO")


