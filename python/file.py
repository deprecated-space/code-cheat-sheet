f = open('Set.py')

try:
  data = f.read()
finally:
  print(data)

f.close()


# pythonic
with open('Set.py') as f: # with 语句自动 close file
  data = f.read()
  print(data)