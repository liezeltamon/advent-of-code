import pandas as pd


df = pd.read_csv("./input_02.txt", sep=" ", header=None)
df = df.set_axis(["direction", "magnitude"], axis=1, inplace=False)

### Part one ###

print(direction_total)

depth = direction_total.at["down"] - direction_total.at["up"]
print(f"Depth: {depth}")
answer = depth * direction_total.at["forward"]
print(f"Depth x Horizontal: {answer}")

### Part two ###

df["horizontal"] = 0 * df.shape[0]
df.loc[df.direction == "forward",
       "horizontal"] = df.loc[df.direction == "forward", "magnitude"]

df["aim"] = df.magnitude
df.loc[df.direction == "forward", "aim"] = 0
df.loc[df.direction == "up", "aim"] = df.loc[df.direction == "up", "aim"] * -1

aim = df.aim.tolist()
df["aim_cumsum"] = [sum(aim[:ind]) for ind in range(0, len(aim), 1)]
df["depth"] = df.horizontal * df.aim_cumsum

print("Depth x Horizontal: ", sum(df.depth) * sum(df.horizontal))
