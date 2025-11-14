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
a = II()
L = [list("+------------------------+"),
     list("|#.#.#.#.#.#.#.#.#.#.#.|D|)"),
     list("|#.#.#.#.#.#.#.#.#.#.#.|.|"),
     list("|#.......................|"),
     list("|#.#.#.#.#.#.#.#.#.#.#.|.|)"),
     list("+------------------------+")]
i = 1
j = 1
f = False
while a:
    if f and i == 3:
        i += 1
    if i == 3:
        f = True
    L[i][j] = 'O'
    if i == 4:
        j += 2
    i = i % 4 + 1


    a -= 1
for i in L:
    print(*i, sep ='')
