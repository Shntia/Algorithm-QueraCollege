import sys
sys.setrecursionlimit(10**6)

inp = int(input())


def f(x):
    if x == 0:
        return 5
    temp = f(x - 1)
    if x % 2 == 0:

        out = temp - 21
        return out

    else:
        return temp ** 2


print(f(inp))
