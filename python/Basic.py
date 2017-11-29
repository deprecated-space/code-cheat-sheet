# [0, 10)
for i in range(0, 10): 
  print(i)


# [0, 5)
for i in range(5): 
  print(i)


# 0, 2, 4, 6, 8
for i in range(0, 10, 2): 
  print(i)


# (0, 1)
# (1, 4)
# (2, 9)
a = [1, 4, 9]
for index, item in enumerate(a):
  print(index, item)


print(isinstance(a, (list, tuple))) # True

from collections import Iterable
print(isinstance([1, 2, 3], Iterable)) # True list 是否可迭代



# map
def f(x):
  return x * x

print(list(map(f, [1, 2, 3])))


# sort
d = {1: 'z', 2:'y', 3: 'x'}
print(sorted(d.items(), key=lambda x: x[1]))


# type 函数查看类型 

# id 函数查看是否是同一引用

a = 10
b = a
print(id(a))
print(id(b))