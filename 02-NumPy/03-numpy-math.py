import numpy as np

d = np.sum

print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    ])
print(d)
print(np.sum(d))
print(np.sum(d[0]))
print(np.sum(d, axis = 0))
print(np.subtract(d[0], d[1]))
print(np.multiply(d[0], d[1]))
