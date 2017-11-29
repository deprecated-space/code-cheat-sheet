## 局部变量和全局变量

```python
a = 10

def changeValue(b):
  global a
  a = b

changeValue(20)
print(a) # 20
```

## 关键字参数

