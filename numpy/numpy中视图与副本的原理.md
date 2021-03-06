---
title: numpy中视图与副本的原理
date: 2021-11-09 20:47:01
tags:
- numpy
- 视图
- 副本
categories:
- numpy
---
副本是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置。

视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。

<!-- more -->

**视图一般发生在：**

- 1、numpy 的切片操作返回原数据的视图。
- 2、调用 ndarray 的 view() 函数产生一个视图。

**副本一般发生在：**

- Python 序列的切片操作，调用deepCopy()函数。
- 调用 ndarray 的 copy() 函数产生一个副本。

### 无复制

简单的赋值不会创建数组对象的副本，只是传递可变对象的引用。 相反，它使用原始数组的相同`id()`来访问它。` id()`返回 Python 对象的通用标识符，类似于 C 中的指针。

此外，一个数组的任何变化都反映在另一个数组上。 例如，一个数组的形状改变也会改变另一个数组的形状。

```python
import numpy as np 
 
a = np.arange(6)  
print ('我们的数组是：')
print (a)
print ('调用 id() 函数：')
print (id(a))
print ('a 赋值给 b：')
b = a 
print (b)
print ('b 拥有相同 id()：')
print (id(b))
print ('修改 b 的形状：')
b.shape =  3,2  
print (b)
print ('a 的形状也修改了：')
print (a)

'''输出结果为：'''
我们的数组是：
[0 1 2 3 4 5]
调用 id() 函数：
4349302224
a 赋值给 b：
[0 1 2 3 4 5]
b 拥有相同 id()：
4349302224
修改 b 的形状：
[[0 1]
 [2 3]
 [4 5]]
a 的形状也修改了：
[[0 1]
 [2 3]
 [4 5]]
```

### 视图或浅拷贝

#### `view()`

`ndarray.view()` 方会创建一个新的数组对象，该方法创建的新数组的维数变化不会改变原始数据的维数。

个人理解：视窗就是真实物理内存中数据的一种表现形式，`b=a.view()` 方会创建一个名为`b`的数组对象，`b`与`a`都指向物理内存中相同的位置。

- 修改`a`的维度，不修改`a`变量的值，`b`将不会有任何变化
- 修改`b`的维度，不修改`a`变量的值，`a`将不会有任何变化
- 修改`a`变量的值，`b`将会有跟着变化
- 修改`b`变量的值，`a`将会有跟着变化

```python
import numpy as np 
 
# 最开始 a 是个 3X2 的数组
a = np.arange(6).reshape(3, 2)
print('数组 a：')
print(a)
print('创建 a 的视图：')
b = a.view()
print(b)
print('两个数组的 id() 不同：')
print('a 的 id()：')
print(id(a))
print('b 的 id()：')
print(id(b))
# 修改 b 的形状，并不会修改 a
b.shape = 2, 3
print('b 的形状：')
print(b)
print('a 的形状：')
print(a)
b[1][1] = 6
print('b的值：')
print(b)
print('a的值也会跟着变化：')
print(a)

'''输出结果为：'''
数组 a：
[[0 1]
 [2 3]
 [4 5]]
创建 a 的视图：
[[0 1]
 [2 3]
 [4 5]]
两个数组的 id() 不同：
a 的 id()：
140349599448880
b 的 id()：
140349599448976
b 的形状：
[[0 1 2]
 [3 4 5]]
a 的形状：
[[0 1]
 [2 3]
 [4 5]]
b的值：
[[0 1 2]
 [3 6 5]]
a的值也会跟着变化：
[[0 1]
 [2 3]
 [6 5]]
```

#### 切片

使用切片创建视图修改数据会影响到原始数组：

```python
import numpy as np 
 
arr = np.arange(12)
print ('我们的数组：')
print (arr)
print ('创建切片：')
a=arr[3:]
b=arr[3:]
a[1]=123
b[2]=234
print(arr)
print(id(a),id(b),id(arr[3:]))

'''输出结果为：'''
我们的数组：
[ 0  1  2  3  4  5  6  7  8  9 10 11]
创建切片：
[  0   1   2   3 123 234   6   7   8   9  10  11]
4545878416 4545878496 4545878576
```

变量 a,b 都是 arr 的一部分视图，对视图的修改会直接反映到原数据中。但是我们观察 a,b 的 id，他们是不同的，也就是说，视图虽然指向原数据，但是他们和赋值引用还是有区别的。

### 副本或深拷贝

`ndarray.copy()` 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。

```python
import numpy as np 
 
a = np.array([[10,10],  [2,3],  [4,5]])  
print ('数组 a：')
print (a)
print ('创建 a 的深层副本：')
b = a.copy()  
print ('数组 b：')
print (b)
# b 与 a 不共享任何内容  
print ('我们能够写入 b 来写入 a 吗？')
print (b is a)
print ('修改 b 的内容：')
b[0,0]  =  100  
print ('修改后的数组 b：')
print (b)
print ('a 保持不变：')
print (a)

'''输出结果为：'''
数组 a：
[[10 10]
 [ 2  3]
 [ 4  5]]
创建 a 的深层副本：
数组 b：
[[10 10]
 [ 2  3]
 [ 4  5]]
我们能够写入 b 来写入 a 吗？
False
修改 b 的内容：
修改后的数组 b：
[[100  10]
 [  2   3]
 [  4   5]]
a 保持不变：
[[10 10]
 [ 2  3]
 [ 4  5]]
```

更多文章：[Python中的深拷贝与浅拷贝](https://huffman-cotdom.github.io/2021/11/09/python%E4%B8%AD%E7%9A%84append%E3%80%81%E6%B5%85%E6%8B%B7%E8%B4%9D%E4%B8%8E%E6%B7%B1%E6%8B%B7%E8%B4%9D/#more)

