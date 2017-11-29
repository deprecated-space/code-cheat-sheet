str = 'hello world'


# 字符串的截取 -> 变量[头下标:尾下标]
print(str[6:11]) # world
print(str[6:]) # world
print(str[-5:]) # world


# repeat
print(str * 2) # hello worldhello world


# concat
print('hello' + ' ' + 'world') # hello world

# len
print(len(str)) # 11


# .strip() 删除字符串首尾空格
print(' hello world   '.strip()) # hello world


for s in 'hello':
  print(s)