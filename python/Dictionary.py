# a dictionary
colors = {
  'red': 1,
  'blue': 2,
  'green': 3
}

print(colors['red']) # 1


# 如果不确定 key 有没有在字典中，先用 in 判断，如果直接取值会报错
if ('yellow' in colors):
  print(colors['yellow'])
else:
  print('no yellow')
 

print(colors.get('pink', 4)) # 4 (4 is the default value)