import numpy as np
import sys
import time

tlist = range(1000)
print(sys.getsizeof(tlist)*len(tlist))

a = np.arange(1000)
print(a.size * a.itemsize)

def using_list():
    t1 = time.time()
    tlist1 = range(10000)
    tlist2 = range(10000)
    z = [tlist1[i] + tlist2[i] for i in range(len(tlist1))]
    
    return time.time()-t1

def using_numpy():
    t1 = time.time()
    tlist1 = np.arange(10000)
    tlist2 = np.arange(10000)
    z = tlist1 + tlist2
    
    return time.time()-t1


def main():
    retval = using_list()
    print(f"Time using list  :{retval}")
    
    retval = using_numpy()
    print(f"Time using numpy :{retval}")
if (__name__ == "__main__"):
    main()
