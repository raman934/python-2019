# RG
# 7.12


def m_in_arr(m, _arr):
    n = len(_arr)
    if n == 0:
        return False
    if m == _arr[0]:
        return True
    else:
        return m_in_arr(m, _arr[1:n])


print(m_in_arr(5, [1, 2, 0, 4, 1]))
