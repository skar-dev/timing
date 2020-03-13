#import timeit
from timeit import Timer
#import numpy as np

#concat
def test1():
    l = []
    for i in range(10000):
        l = l + [i]

#append
def test2():
    l = []
    #Add a new element with append
    for i in range(10000):
        l.append(i)

#comprehension
def test3():
    #Use bracket that contains elements
    #l =
    [i for i in range(10000)]

#list range
def test4():
    #Use list method
    #l =
    list(range(10000))

expSize = 10

t1 = Timer("test1()", "from __main__ import test1")
st1 = t1.timeit(number=expSize)
print("concat ",st1, "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=expSize), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=expSize), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
st4 = t4.timeit(number=expSize)
print("list range ",st4, "milliseconds")

print ('\n Worst vs. best ratio', st1/st4, '\n')
