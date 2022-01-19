import numpy as np
import pandas as pd

which_part = 1  # 1 or 2
######################

df = pd.read_table("input_05.txt", sep=" ", header=None)
df
df[[0, 1]] = df.iloc[:, 0].str.split(",", expand=True)
df[[2, 3]] = df.iloc[:, 2].str.split(",", expand=True)

df.columns = ["x1", "y1", "x2", "y2"]
df = df.loc[:, ["x1", "x2", "y1", "y2"]].astype("int64")

# Identify horizontal/vertical segments/points
for axis in ["x", "y"]:
    df_arr = df.loc[:, [axis + "1", axis + "2"]].to_numpy()
    df[axis + "_diff"] = np.diff(df_arr).squeeze()

df["is_horver"] = (df.x_diff.values * df.y_diff.values) == 0
df["is_diagonal"] = (np.abs(df.x_diff.values) == np.abs(df.y_diff.values)) * (
    np.abs(df.x_diff.values) > 1)

# Subset horizontal/vertical segments/points

if which_part == 1:
    df = df[df.is_horver.values]
elif which_part == 2:
    df = df[df.is_horver.values + df.is_diagonal.values]
else:
    print("Invalid which_part value.")

segment_len = len(df)

# Fill array

np.max(df.iloc[:, 0:4].to_numpy())  # 989

points_arr = np.zeros(shape=(1000, 1000), dtype="int64")
for i in range(segment_len):

    print(i, "...")

    xbds = sorted([df.loc[:, "x1"].iloc[i], df.loc[:, "x2"].iloc[i]])
    ybds = sorted([df.loc[:, "y1"].iloc[i], df.loc[:, "y2"].iloc[i]])

    xinds = [*range(xbds[0], xbds[1] + 1)]
    yinds = [*range(ybds[0], ybds[1] + 1)]

    if df.loc[:, "x_diff"].iloc[i] < 1:
        xinds.reverse()

    if df.loc[:, "y_diff"].iloc[i] < 1:
        yinds.reverse()

    points_arr[xinds, yinds] = points_arr[xinds, yinds] + 1

print("Ans part ", which_part, ": ", np.sum(points_arr >= 2))
