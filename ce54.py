# RG
# 4.16

from ce39 import temperature


def temperature_loop(start, end, step):
    for i in range(start, end+1, step):
        print("%d : " % i, end='')
        print(int(temperature(i)))


temperature_loop(0, 100, 20)
