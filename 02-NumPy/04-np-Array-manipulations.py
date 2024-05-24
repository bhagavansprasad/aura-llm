# Indexing
import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
)

print (f"a         :\n{a}")
print (f"a[0]      :{a[0]}")
print (f"a[:1]     :{a[:1]}")
print (f"a[:1,1:]  :{a[:1,1:]}")
print (f"a[2:,2:]  :{a[2:,:2]}")
print (f"a[:2,1:]  :{a[:2,1:]}")
print (f"a[1:,2:]  :{a[1:,1:]}")
