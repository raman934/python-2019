# RG
# 7.9 # todo for input 7, works only till 6
memory = [0]*1000
temp = [0]*1000


def pattern_3(n):
    if max(memory) < n:
        memory[n] = n
    if n == 0:
        return None
    x = max(memory) - n + 1
    for j in range(x):
        if j == 0 or j == x-1:
            print(1, end=' ')
        elif j == 1 or j == x-2:
            print(x-1, end=' ')
            temp[x] = x-1
        else:
            temp_ = temp[x - 1] + (2 * temp[x - 2])
            if x == 5:
                temp_2 = 2*temp[x - 1]
                print(temp_2, end=' ')
            else:
                print(temp_, end=' ')
    print()
    pattern_3(n - 1)


pattern_3(6)
