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
s = I()
ans = 0
while "Danil" in s:
    ans += 1
    s = s.replace("Danil", '_', 1)
while "Olya" in s:
    ans += 1
    s = s.replace("Olya", '_', 1)
while "Slava" in s:
    ans += 1
    s = s.replace("Slava", '_', 1)
while "Ann" in s:
    ans += 1
    s = s.replace("Ann", '_', 1)
while "Nikita" in s:
    ans += 1
    s = s.replace("Nikita", '_', 1)

# print(s)
print("YES" if ans == 1 else "NO")