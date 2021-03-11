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


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
    print(fib_list(n))
