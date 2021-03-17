# Uses python3
import sys


def lcm(a, b):
    if (b % a == 0 and b > a):
        return b
    for l in range(b, a * b + 1, b):
        if (l % a == 0 and l % b == 0):
            return l


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm(a, b))
