# RG
# 7.13
memory = [0]*1000


def m_position(m, _arr):

    n = len(_arr)
    if n == 0:
        return -1
    if m == _arr[0]:
        return max(memory)
    else:
        memory[m] += 1
        return m_position(m, _arr[1:n])


print(m_position(5, [1, 5, 3, 4, 5]))
