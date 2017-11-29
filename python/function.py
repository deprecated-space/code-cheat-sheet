def printInfo(name, age, sex='m', nationality='China'): # 默认参数在最后
  print(name, age, sex, nationality)

printInfo('hanzichi', 30, 'f')
printInfo('hanzichi', 30, nationality='Japan')


def getSum(*num):
  sum = 0
  for val in num:
    sum += val 
  return sum

print(getSum(1, 2, 3, 4)) # 10


# 关键字参数
def printInfo2(name, age=30, **kw): # 默认参数在最后
  print(name, age, kw)

# hanzichi 30 {'sex': 'f', 'nationality': 'China'} kw 其实是一个 dict
printInfo2('hanzichi', 30, sex='f', nationality='China') 

