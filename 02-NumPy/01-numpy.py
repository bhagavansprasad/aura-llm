import numpy as np

a = np.array([3,5,7,8,9])
print(a)

b = np.array([[3,5,7],[2, 5, 9]])
print(b)

c = np.zeros((3, 4))
print(c)


d = np.arange(10,25,5)
print("d")
print(d)

e = np.arange(1, 10, 2)
print("e")
print(e)

# help(np.linspace)
f = np.linspace(5, 10, 10)
print("f")
print(f)

g = np.linspace(0,10,6)
print("g")
print(g)

print()
d = np.full((2,3), 5)
print(d)

print()
d = np.random.random((2,3))
print(d)