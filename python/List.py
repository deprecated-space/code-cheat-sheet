a = [1, 2, 3, 4, 5]


# 截取 -> 列表[头下标:尾下标]
print(a[2:4]) # [3, 4]
print(a[2:]) # [3, 4, 5]
print(a[-3:]) # [3, 4, 5]


# repeat
print(a * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# concat
print([1, 2, 3] + [4, 5]) # [1, 2, 3, 4, 5]


# del
b = [1, 2, 3, 4]
del b[2]
print(b) # [1, 2, 4]


# 函数 & 方法
print(max(a)) # 5
print(min(a)) # 1


a.append(6)
print(a) # [1, 2, 3, 4, 5, 6]


a.extend([7, 8])
print(a) # [1, 2, 3, 4, 5, 6, 7, 8]

a.extend('78') # [1, 2, 3, 4, 5, 6, 7, 8, '7', '8']
print(a)


# 复制数组
e = a[:]
print(e)


# 统计某个元素在列表中出现的次数
c = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(c.count(3)) # 3


# 初始化数组
d = [None] * 5
print(d) # [None, None, None, None, None]


# 列表解析
print([n * n for n in range(1, 11)])

# 筛选
nums = [-1, 0, 1, 2, 3]
res = [n for n in nums if n > 0]
print(res) # [1, 2, 3]

