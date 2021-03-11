# python3
import random


def naive_max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product(numbers):
    index1 = 0
    n = len(numbers)
    for index in range(1, n):
        if numbers[index] > numbers[index1]:
            index1 = index
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for index in range(1, n):
        if index != index1 and numbers[index] > numbers[index2]:
            index2 = index
    # print('num1: ' + str(numbers[index1]) + ', num2: ' + str(numbers[index2]))
    return numbers[index1] * numbers[index2]


def streess_test(N, M):
    while True:
        n = random.randint(2, N)
        print('n: ' + str(n))
        input_numbers = []
        for i in range(n):
            input_numbers.append(random.randint(0, M))
        print(input_numbers)
        result1 = max_pairwise_product(input_numbers)
        result2 = naive_max_pairwise_product(input_numbers)
        if result1 == result2:
            print('Ok')
        else:
            print('Wrong answer: ' + str(result1) + ', ' + str(result2))
            break


if __name__ == '__main__':
    # streess_test(1000, 200000)

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
