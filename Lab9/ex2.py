import numpy as np


def run_length_encoding(x):
    unique_values = []
    counts = []
    current_value = x[0]
    count = 1

    for value in x[1:]:
        if value == current_value:
            count += 1
        else:
            unique_values.append(current_value)
            counts.append(count)
            current_value = value
            count = 1
    unique_values.append(current_value)
    counts.append(count)

    return (np.array(unique_values), np.array(counts))


x = np.array([2, 2, 2, 3, 3, 3, 5])
print(run_length_encoding(x))
