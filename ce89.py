# RG
# 7.6 # todo learn method of memorization
memory = [None]*1000


def fibonacci(n):
    if memory[n] is not None:
        return memory[n]
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    memory[n] = result
    return result


print(fibonacci(8))
