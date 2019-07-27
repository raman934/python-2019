# RG
# 4.14
# todo try again... P.s. this is Sir's Method


def sequence(n):
    prev = float('inf')                 # gave it infinity value
    state = 'dec'
    for i in range(n):
        a = int(input('Enter %d term:\t' % i))
        if state == 'dec':
            if prev > a:
                prev = a
            elif prev == a:
                return False
            else:
                state = 'inc'
                prev = a
        else:
            if prev < a:
                prev = a
            else:
                return False
    return True


print(sequence(9))
