# RG
# 7.15

# N = int(input("Enter the size of the array :\t"))
arr = [1, 2, 3]

# for i in range(N):
#     arr[i] = int(input("Enter :\t"))

# for i in range(4):
#     for j in range(i, 4):
#         print(arr[i:j], end='   ')
# x = [1, 2, 3]
memory = []
temp = 1


def function(x):
    n = len(x)
    memory.append(x)
    if n > 0 and temp == 1:
        return function(x[:n-1])
    temp = 0
    return memory


print(function([1, 2, 3]))
