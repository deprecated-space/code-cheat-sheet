import math
print(dir(math)) # dir 可列出模块所有函数，暂时可以不考虑 __ 开头的函数
print(dir(__builtins__)) # 查看 py 内置函数，可以看到内置和 math 都有 pow 函数
print(dir('')) # 查看字符串拥有的函数
print(dir())


print(help(math.sin)) # 查看函数文档
print(math.sin.__doc__) # 作用同上


print('1', '2', '3') # 1 2 3
print('1', '2', '3', sep=';') # 1;2:3
print(1, 2, end=' ')
print(3, 4) # 1 2 3 4

