## 字符串

|       函数名       |         什么情况下返回 True          |
| :-------------: | :---------------------------: |
|  s.endswith(t)  |                               |
| s.startswith(t) |                               |
|   s.isalnum()   |          s 只包含字母或数字           |
|   s.isalpha()   |            s 只包含字母            |
|  s.isdecimal()  |        s 只包含表示十进制数字的字符        |
|   s.isdigit()   |           s 只包含数字字符           |
|   s.islower()   |           s 只包含小写字母           |
|   s.isupper()   |                               |
|  s.isnumeric()  |            s 只包含数字            |
|   s.isspace()   |           s 只包含空白字符           |
|   s.istitle()   | s 是个大小写符合标题要求（title-case）的字符串 |
|     t in s      |                               |

|         函数名         |                   返回值                    |
| :-----------------: | :--------------------------------------: |
|      ord('a')       |               Unicode 码，97               |
|       chr(97)       |                   'a'                    |
|      s.find(t)      |              -1 or 第一次出现的位置              |
|     s.rfind(t)      |               从右往左搜索，返回如上                |
|     s.index(t)      |         和 find 类似，如果没找到 t，则引发异常          |
|     s.rindex(t)     |                                          |
|   s.capitalize()    |             将 s[0] 改为大写，其余小写             |
|      s.lower()      |                                          |
|      s.upper()      |                                          |
|    s.swapcase()     |            将小写字母改为大写，大写字母改为小写            |
|      s.title()      |             将 s 的大小写符合标题的要求              |
|   s.center(n, ch)   |     包含 n 个字符的字符串，其中 s 位于中央，两边用 ch 填充     |
|   s.ljust(n, ch)    |                                          |
|   s.rjust(n, ch)    |                                          |
|   s.format(vars)    |                                          |
|     s.strip(ch)     | 从 s 开头和末尾删除所有包含在字符串 ch 中的字符，如果不加参数，则删除空白字符 |
|    s.lstrip(ch)     |                                          |
|    s.rstrip(ch)     |                                          |
|   s.partition(t)    | 将 s 拆分为三个字符串（head、t 和 tail），其中 head 为 t 前面的字串，tail 为 t 后面的字串 |
|   s.rpartition(t)   |                                          |
|     s.split(t)      |                                          |
|     s.join(seq)     | `';'.join(['1', '2', '3'])` 返回字符串 `1:2:3` **注意数组 seq 中的元素必须是字符串 ** |
|     s.rsplit(t)     |                                          |
|   s.splitlines()    |            返回一个由 s 中的各行组成的列表             |
| s.replace(old, new) |                                          |
|     s.count(t)      |               t 在 s 中出现的次数               |
|   s.zfill(width)    |       在 s 左边添加足够的 0，让字符串的长度为 width       |


## 元祖

| 函数名          | 返回值  |
| ------------ | ---- |
| x in tup     |      |
| len(tup)     |      |
| tup.count(x) |      |
| tup.index(x) |      |


## 列表

| 函数名            | 返回值                    |
| -------------- | ---------------------- |
| s.append(x)    | 在列表 s 末尾添加元素 x         |
| s.count(x)     |                        |
| s.extend(lst)  | 将 lst 的所有元素都添加到列表 s 末尾 |
| s.index(x)     |                        |
| s.insert(i, x) |                        |
| s.pop(i)       |                        |
| s.remove(x)    | 删除 s 中第一个 x 元素         |
| s.reverse()    |                        |
| s.sort()       |                        |


## 字典

| 函数名                  | 返回值                                      |
| -------------------- | ---------------------------------------- |
| d.items()            |                                          |
| d.keys()             |                                          |
| d.values()           |                                          |
| d.get(key, default)  |                                          |
| d.pop(key)           | 删除并返回                                    |
| d.popitem()          | 删除字典 d 中 **任意** 键值对并返回                   |
| d.clear()            |                                          |
| d.copy()             |                                          |
| d.fromkeys(s, t)     | 创建一个新的字典，其中的键来自 s，值来自 t                  |
| s.setdefault(key, v) | 如果键 key 包含在字典 d 中，则返回其值；否则，返回 v 并将（key, v) 添加到字典 d 中 |
| s.update(e)          | 将 e 中的键值对添加到字典 d 中；e 可能是字典，也可能是键值对       |

