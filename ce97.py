# RG
# 7.14
memory = [100]*1000


def m_position(m, _arr):
    n = len(_arr)
    memory[n] = n - 1
    if n == 0:
        return -1
    if m == _arr[n-1]:
        return min(memory)
    else:
        return m_position(m, _arr[0:n-1])


print(m_position(5, [1, 5, 5, 4, 0]))
