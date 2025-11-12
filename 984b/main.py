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
n, m = MII()
L = [[0 for _ in range(m)] for _ in range(n)]
M = []
for _ in range(n):
    M.append(list(I()))


for i in range(n):
    for j in range(m):
        if M[i][j] == '*':
            L[i][j] = '*'
            if i > 0 and j > 0 and M[i - 1][j - 1] != '*':
                L[i - 1][j - 1] += 1

            if i > 0 and M[i - 1][j] != '*':
                L[i - 1][j] += 1

            if i > 0 and j < m - 1 and M[i - 1][j + 1] != '*':
                L[i - 1][j + 1] += 1

            if i < n - 1 and j > 0 and M[i + 1][j - 1] != '*':
                L[i + 1][j - 1] += 1

            if i < n - 1 and M[i + 1][j] != '*':
                L[i + 1][j] += 1

            if i < n - 1 and j < m - 1 and M[i + 1][j + 1] != '*':
                L[i + 1][j + 1] += 1

            if j > 0 and M[i][j - 1] != '*':
                L[i][j - 1] += 1
            if j < m - 1 and M[i][j + 1] != '*':
                L[i][j + 1] += 1
for i in range(n):
    f = True
    for j in range(m):
        if L[i][j] == 0 and M[i][j] == '*':
            continue
        elif L[i][j] == '*' and M[i][j] == '*':
            continue
        elif L[i][j] == 0 and M[i][j] == '.':
            continue
        elif M[i][j].isdigit() and L[i][j] == int(M[i][j]):
            continue
        else:
            print("NO")
            f = False
            break
    if not f:
        break
else:
    print("YES")
