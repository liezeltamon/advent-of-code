from pathlib import Path
import numpy as np

days = 256

#####

path = Path("./input_06.txt")
init = str.splitlines(path.read_text())
init = init[0].split(",")

init_arr = np.array(init, dtype="int64")
del init

counter_d = 0
curr_arr = init_arr
del init_arr

for d in range(days):

    counter_d = counter_d + 1
    print(counter_d)
    zero_ind = list(np.where(curr_arr == 0)[0])
    zero_ind_len = len(zero_ind)

    curr_arr = curr_arr - 1

    if zero_ind_len > 0:
        curr_arr[zero_ind] = 6
        curr_arr = np.append(curr_arr,
                             np.repeat(8, zero_ind_len))

    del zero_ind

print(curr_arr.shape[0], " lanternfishes after ", days, " days!")
