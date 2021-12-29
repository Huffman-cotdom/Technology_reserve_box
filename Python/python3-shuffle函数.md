---
title: python3_shuffle函数
date: 2021-11-10 15:59:32
tags:
- Python
categories:
- Python
---
`shuffle()`方法将序列的所有元素随机排序。
<!-- more -->

```python
import random
 
random.shuffle (lst)
```

`shuffle()` 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

```python
import random
 
list = [20, 16, 10, 5];
random.shuffle(list)
print ("随机排序列表 : ",  list)
 
random.shuffle(list)
print ("随机排序列表 : ",  list)

'''输出结果'''
随机排序列表 :  [20, 5, 16, 10]
随机排序列表 :  [5, 20, 10, 16]
```

如果想使用相同种子使得随机排序后结果相同。

```python
import random

list = [20, 16, 10, 5]
random.seed(10)
random.shuffle(list)
print("随机排序列表 : ", list)
random.seed(10)
random.shuffle(list)
print("随机排序列表 : ", list)

'''输出结果'''
随机排序列表 :  [5, 10, 16, 20]
随机排序列表 :  [20, 16, 10, 5]
```

可以看出每次shuffle得到的结果并不相同。

`random.shuffle` 具有破坏性，需要每次都重置列表。

```python
import random

SEED = 10
original_list = ['list', 'elements', 'go', 'here']
random.seed(SEED)
my_list = original_list[:]
random.shuffle(my_list)
print("RUN1: ", my_list)
random.seed(SEED)
my_list = original_list[:]
random.shuffle(my_list)
print("RUN2: ", my_list)

'''输出结果：'''
RUN1:  ['here', 'go', 'elements', 'list']
RUN2:  ['here', 'go', 'elements', 'list']
```

