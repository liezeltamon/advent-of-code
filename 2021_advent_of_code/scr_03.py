import numpy as np
from pathlib import Path


def inputbits_to_array(input_path):
    bits = np.loadtxt(input_path, dtype="str", delimiter=" ")
    bits_array = []

    for bit_str in bits:
        bits_array.append([*bit_str])

    bits_array = np.array(bits_array)
    bits_array = bits_array.astype(int)

    return(bits_array)


def dominant_bit(bits_array, default_bit_ties, return_rare_bit):
    items_len = len(bits_array)
    column_sum = np.sum(bits_array, axis=0)

    if not default_bit_ties in [0, 1]:
        print("Unexpected default_bit_ties argument.")

    bits_out = np.zeros(column_sum.shape, dtype=int)
    bits_out[column_sum > (items_len / 2)] = 1

    if return_rare_bit:
        bits_out = (bits_out - 1) * -1

    bits_out[column_sum == (items_len / 2)] = default_bit_ties

    return(bits_out)


### Part one ###

# bits_array = inputbits_to_array(Path("./input_03.txt"))
# print(bits_array)

# gamma = dominant_bit(bits_array, default_bit_ties=None, return_rare_bit=False)
# print(gamma)

# epsilon = dominant_bit(bits_array, default_bit_ties=None, return_rare_bit=True)

# rates_str = [rate.astype(str).tolist() for rate in [gamma, epsilon]]
# power_consumption = [int("".join(rate), 2) for rate in rates_str]
# print(np.prod(np.array(power_consumption)))


### Part two ###

bits_array = inputbits_to_array(Path("./input_03.txt"))
items_len = len(bits_array)
col_len = np.shape(bits_array)[1]

for bit_ties in [0, 1]:

    bits_array_reduced = bits_array
    is_return_rare_bit = {"0": True, "1": False}[str(bit_ties)]

    for pos in range(0, col_len, 1):
        filtering_col = bits_array_reduced[:, pos:(pos+1)]

        dominant = dominant_bit(
            filtering_col, default_bit_ties=bit_ties, return_rare_bit=is_return_rare_bit)
        bits_array_reduced = bits_array_reduced[filtering_col.squeeze(
        ) == dominant, :]
        items_len = len(bits_array_reduced)

        if (items_len == 1) & (bit_ties == 1):
            oxygen = bits_array_reduced.squeeze()
            print("Oxygen rating identified")
            break
        elif (items_len == 1) & (bit_ties == 0):
            scrubber = bits_array_reduced.squeeze()
            print("C02 scrubber rating identified")
            break
        else:
            print("Searching...")

print(oxygen, scrubber)

rates_str = [rate.astype(str).tolist() for rate in [oxygen, scrubber]]
print(rates_str)
life_support = [int("".join(rate), 2) for rate in rates_str]
print(life_support)
print(np.prod(np.array(life_support)))
