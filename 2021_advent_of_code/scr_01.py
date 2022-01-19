from pathlib import Path
import numpy as np


### Part one ###

path = Path("./input_01.txt")
values = str.splitlines(path.read_text())
values = [int(val) for val in values]

values = np.array(values)
print(sum(np.diff(values) > 0))

### Part two ###

path = Path("./input_01.txt")
values = str.splitlines(path.read_text())
values = [int(val) for val in values]

values_len = len(values)

values_window = [sum(values[ind:(ind + 3)])
                 for ind in range(0, values_len - 2, 1)]

values_window = np.array(values_window)
print(sum(np.diff(values_window) > 0))

# Try with pandas, or package with groupBy function
