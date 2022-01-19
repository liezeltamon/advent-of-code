from pathlib import Path
import numpy as np
import pandas as pd
import math

part = 1

#####

path = Path("./input_07.txt")
hor_pos = str.splitlines(path.read_text())
hor_pos = hor_pos[0].split(",")
hor_pos = np.array(hor_pos, dtype="int")

hor_pos_pd = pd.Series(hor_pos)
pos_counts = hor_pos_pd.value_counts()

# Candidate best horizontal positions

pos_maxcount = int(pos_counts.idxmax())
mean_val = np.mean(hor_pos)
med_val = np.median(hor_pos)

candidates = [pos_maxcount, math.floor(mean_val),
              math.ceil(mean_val), med_val]
candidates = np.unique(np.array(candidates, dtype="int64"))
candidates = np.intersect1d(candidates, hor_pos)
candidates = candidates.tolist()

# Calculate fuel per candidate

cand_len = len(candidates)
hor_pos_len = len(hor_pos)
fuel = np.zeros(shape=(cand_len,), dtype="int64")
for i in range(cand_len):

    poscand_diff = np.abs(hor_pos - candidates[i])

    if part == 1:
        fuel[i] = np.sum(poscand_diff)
    elif part == 2:

        part2_fuel = np.zeros(shape=(hor_pos_len,), dtype="int64")
        for f in range(hor_pos_len):
            part2_fuel[f] = sum(range(1, poscand_diff[f] + 1, 1))
        fuel[i] = np.sum(part2_fuel)

    else:
        print("invalid part argument.")

min_fuel = np.min(fuel)
minfuel_ind = np.where(fuel == min_fuel)[0][0]
ans_pos = candidates[minfuel_ind]

# Optimal position for Part 1 and 2 are mean and floor(mean) values, respectively.
print(f"Part {part} - Position: {ans_pos}; Total fuel: {min_fuel}")
