# Каждый новый член в последовательности Фибоначчи генерируется путем добавления двух предыдущих членов.
# Начиная с 1 и 2, первые 10 терминов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Рассмотрев члены последовательности Фибоначчи, значения которых не превышают
# четырех миллионов, найдите сумму четных членов.


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sum_fib_even(limit):
    i = mysum = 0
    while fib(i) <= limit:
        if fib(i) % 2 == 0:
            mysum += fib(i)

        i += 1

    return mysum


if __name__ == '__main__':
    print(sum_fib_even(4000000))