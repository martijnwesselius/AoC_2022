import numpy as np

calorie_per_elf = []

with open('file_day1.txt') as f:
    calorie_list = f.read().splitlines()
    c = 0
    for i in calorie_list:
        if i != '':
            c = c + int(i)
        else:
            calorie_per_elf.append(c)
            c=0

calorie_per_elf = np.array(calorie_per_elf)

max_cal = np.max(calorie_per_elf)
print(max_cal)

top3_cal = np.sort(calorie_per_elf)[-3:]
sum3_cal = np.sum(top3_cal)
print(sum3_cal)

