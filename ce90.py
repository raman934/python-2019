# RG
# 7.7
memory = [0]*1000


def pattern_1(n):
    if max(memory) < n:
        memory[n] = n
    if n == 0:
        return None
    print('* '*(max(memory) - n + 1), end='')
    print()
    pattern_1(n-1)


pattern_1(5)
