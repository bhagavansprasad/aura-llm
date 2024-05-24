import numpy as np

print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    [0, 1, 3],
    [6, 2, 7],
    ])
print(d.shape)

print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    ])
print(d.shape)

print()
d.shape = (3,2)
print(d.shape)
print(d)

print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    [0, 1, 3],
    [6, 2, 7],
    ])
print(d.shape)
print(d)
d.shape = (6,2)
print(d.shape)
print(d)

print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    [0, 1, 3],
    [6, 2, 7],
    ])
print(d.ndim)

print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    [0, 1, 3],
    [6, 2, 7],
    ])
d.shape = (2,3,2)
print(d.ndim)
print(d.shape)
print(d)

print()
d = np.arange(24)
d.shape = (3,4,2)
print(d.ndim)
print(d.shape)
print(d)
print(d.size)


print()
d = np.array([
    [5, 6, 7],
    [4, 7, 8],
    [0, 1, 3],
    [6, 2, 7],
    ])
print(d.size)

print()
d = np.array([[5, 6, 7], [4, 7, 8], [6, 2, 7]])
print(d.size)

print()
d = np.arange(24, dtype=float)
print(d.size)
print(d.dtype)
print(d)
