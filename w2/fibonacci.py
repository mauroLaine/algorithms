# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def fib_list(n):
    number_list = [None] * (n + 1)
    number_list[0] = 0
    number_list[1] = 1
    for i in range(2, n + 1):
        number_list[i] = number_list[i - 1] + number_list[i - 2]
        # print(number_list)
    return number_list[n]


def fib_mod(n, m):
    pisano, previous, current = 0, 0, 0
    for i in range(2, (m * m) + 1):
        previous = current
        fnP = fib_list(i)
        current = fnP % m
        # print('f(' + str(i) + '): ' + str(fnP) + ' | ' + str(previous) + ', ' + str(current))
        if i > 2 and previous == 0 and current == 1:
            pisano = i - 1
            break
    nP = n % pisano
    return fib_list(nP) % m


if __name__ == '__main__':
    # Fibonacci number
    # n = int(input())
    # print(calc_fib(n))
    # print(fib_list(n))

    # Fibonacci mod
    input = input()
    n, m = map(int, input.split())
    print(fib_mod(n, m))
