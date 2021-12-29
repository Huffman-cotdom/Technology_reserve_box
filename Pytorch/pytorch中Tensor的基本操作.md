---
title: PyTorch中Tensor的基本操作
date: 2021-11-09 17:43:47
tags:
- PyTorch
- Tensor
categories:
- PyTorch
---
PyTorch中Tensor的基本操作记录

<!-- more -->

## Tensor的维度

```python
z = torch.ones(2, 3, 4)
print(z)
print(z.size())
print(z.size(0))
print(z.size(1))
print(z.size(2))

'''运行结果'''
tensor([[[1., 1., 1., 1.],
         [1., 1., 1., 1.],
         [1., 1., 1., 1.]],

        [[1., 1., 1., 1.],
         [1., 1., 1., 1.],
         [1., 1., 1., 1.]]])
torch.Size([2, 3, 4])
2
3
4
```

第一层（最外层）中括号里面包含了两个中括号（以逗号进行分割），这就是（2，3，4）中的2。

第二层中括号里面包含了三个中括号（以逗号进行分割），这就是（2，3，4）中的3。

第三层中括号里面包含了四个数（以逗号进行分割），这就是（2，3，4）中的4。

### 结论

pytorch中的tensor维度可以通过第一个数前面的中括号数量来判断，有几个中括号维度就是多少。拿到一个维度很高的向量，将最外层的中括号去掉，数最外层逗号的个数，逗号个数加一就是最高维度的维数，如此循环，直到全部解析完毕。

`z.size(0) = 2，z.size(1) = 3，z.size(2) = 4`

第0维度为2，第1维度为3，第2维度为4，即**维度的标号是以0开始的**。

## squeeze & unsqueeze

### squeeze

```python
torch.squeeze(input, dim=None, out=None) → Tensor
```

**当不给定dim时**，除去输入张量input中数值为1的维度，并返回新的张量。

例如：如果输入张量的形状为`（ A × 1 × B × C × 1 × D ）`，那么输出张量的形状为`（ A × B × C × D ）`。

**当通过dim参数指定维度时**，维度压缩操作只会在指定的维度上进行。如果输入向量的形状为`（ A × 1 × B ）` ，`squeeze(input, 0)`会保持张量的维度不变，只有在执行`squeeze(input, 1)`时，输入张量的形状会被压缩至`（ A × B ）`。

> **注意：**
>
> If the tensor has a batch dimension of size 1, then squeeze(input) will also remove the batch dimension, which can lead to unexpected errors.
>
> 如果张量具有尺寸为1的批量尺寸，则squeeze（input）也将移除批处理维度，但是会导致意外错误。
>
> ```python
> x = torch.zeros(1)
> print(x, x.shape)
> print(x.squeeze(), x.squeeze().shape)
> x = torch.randn(1, 1)
> print(x, x.shape)
> print(x.squeeze(), x.squeeze().shape)
> 
> '''运行结果'''
> tensor([0.]) torch.Size([1])
> tensor(0.) torch.Size([])
> tensor([[-0.6311]]) torch.Size([1, 1])
> tensor(-0.6311) torch.Size([])
> ```
>
> 输出的张量与原张量共享内存，如果改变其中的一个，另一个也会改变。

**参数：**

- input (Tensor) – 输入张量
- dim (int, optional) – 如果给定，则`input`只会在给定维度挤压，维度的索引（从0开始）
- out (Tensor, optional) – 输出张量

```python
x = torch.zeros(2, 1, 2, 3, 2)
print(x.size())
y = torch.squeeze(x)
print(y.size())
y = torch.squeeze(x, 0)
print(y.size())
y = torch.squeeze(x, 1)
print(y.size())

'''运行结果'''
torch.Size([2, 1, 2, 3, 2])
torch.Size([2, 2, 3, 2])
torch.Size([2, 1, 2, 3, 2])
torch.Size([2, 2, 3, 2])
```

### unsqueeze

```python
torch.unsqueeze(input, dim, out=None) → Tensor
```

返回一个新的张量，对输入的指定位置插入维度 1。

> **注意:**
>
> 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。

`dim`的值必须在`[-input.dim() - 1, input.dim() + 1)` 之间。如果`dim`为负，则将会被转化`dim =dim + input.dim() + 1`。

**参数:**

- tensor (Tensor) – 输入张量
- dim (int) – 插入维度的索引（从0开始）
- out (Tensor, optional) – 结果张量

```python
a = torch.rand(4, 1, 28, 28)
print(a.shape)
print(a.unsqueeze(0).shape)
b = torch.tensor([1.2, 2.3])
print(b.size())
print(b.unsqueeze(0), b.unsqueeze(0).shape)
print(b.unsqueeze(-1), b.unsqueeze(-1).shape)
x = torch.rand(3)
y = torch.rand(4, 32, 14, 14)
print(x, x.shape)
print(x.unsqueeze(1), x.unsqueeze(1).shape)
x = x.unsqueeze(1).unsqueeze(2).unsqueeze(0)  # [32]->[32,1]->[32,1,1]->[1,32,1,1]
print(x, x.shape)

'''运行结果'''
torch.Size([4, 1, 28, 28])
torch.Size([1, 4, 1, 28, 28])
torch.Size([2])
tensor([[1.2000, 2.3000]]) torch.Size([1, 2])
tensor([[1.2000],
        [2.3000]]) torch.Size([2, 1])
tensor([0.0678, 0.0887, 0.1522]) torch.Size([3])
tensor([[0.0678],
        [0.0887],
        [0.1522]]) torch.Size([3, 1])

tensor([[[[0.0678]],

         [[0.0887]],

         [[0.1522]]]]) torch.Size([1, 3, 1, 1])
```

## reshape & view

`view()`：也就是视图操作，具体可以参考：[pytorch中Tensor的存储原理](https://huffman-cotdom.github.io/2021/11/09/pytorch%E4%B8%ADTensor%E7%9A%84%E5%AD%98%E5%82%A8%E5%8E%9F%E7%90%86/#more)、[numpy中视窗与副本的原理](https://huffman-cotdom.github.io/2021/11/09/numpy%E4%B8%AD%E8%A7%86%E7%AA%97%E4%B8%8E%E5%89%AF%E6%9C%AC%E7%9A%84%E5%8E%9F%E7%90%86/#more)

视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。

### torch.Tensor.view()

```python
view(*shape) → Tensor
```

类似于reshape，将tensor转换为指定的shape，原始的数据不改变。返回的tensor与原始的tensor共享存储区。返回的tensor的size和stride必须与原始的tensor兼容。每个新的tensor的维度必须是原始维度的子空间，或满足以下连续条件，即Tensor必须是连续的空间：

$$
stride[i]=stride[i+1]*size[i+1]
$$
否则需要先使用`contiguous()`方法将原始tensor转换为满足连续条件的tensor，然后就可以使用`view()`进行shape变换了。或者直接使用reshape方法进行维度变换，但这种方法变换后的tensor就不是与原始tensor共享内存了，而是被**重新开辟了一个空间**。

```python
import torch
a = torch.arange(9).reshape(3, 3)      # 初始化张量a
print('storage of a:\n', a.storage())  # 查看a的stride
print('+++++++++++++++++++++++++++++++++++++++++++++++++')
b = a.permute(1, 0).contiguous()       # 转置,并转换为符合连续性条件的tensor
print('size    of b:', b.size())       # 查看b的shape
print('stride  of b:', b.stride())     # 查看b的stride
print('viewd      b:\n', b.view(9))    # 对b进行view操作，并打印结果
print('+++++++++++++++++++++++++++++++++++++++++++++++++')
print('storage of a:\n', a.storage())  # 查看a的存储空间
print('storage of b:\n', b.storage())  # 查看b的存储空间
print('+++++++++++++++++++++++++++++++++++++++++++++++++')
print('ptr of a:\n', a.storage().data_ptr())  # 查看a的存储空间地址
print('ptr of b:\n', b.storage().data_ptr())  # 查看b的存储空间地址
 
'''   运行结果   '''
storage of a:
  0
 1
 2
 3
 4
 5
 6
 7
 8
[torch.LongStorage of size 9]
+++++++++++++++++++++++++++++++++++++++++++++++++
size    of b: torch.Size([3, 3])
stride  of b: (3, 1)
viewd      b:
 tensor([0, 3, 6, 1, 4, 7, 2, 5, 8])
+++++++++++++++++++++++++++++++++++++++++++++++++
storage of a:
 0
 1
 2
 3
 4
 5
 6
 7
 8
[torch.LongStorage of size 9]
storage of b:
 0
 3
 6
 1
 4
 7
 2
 5
 8
[torch.LongStorage of size 9]
+++++++++++++++++++++++++++++++++++++++++++++++++
ptr of a:
 1842671472000
ptr of b:
 1842671472128
```

`contiguous()`方法开辟了一个新的存储区给b，并改变了b原始存储区数据的存放顺序。这种开辟一个新的内存区的方式其实就是深拷贝。

### torch.reshape()

```python
torch.reshape(input, shape) → Tensor
```

与view方法类似，将输入tensor转换为新的shape格式。

但是reshape方法更强大，可以认为`a.reshape = a.view() + a.contiguous().view()`。

即：在满足tensor连续性条件时，`a.reshape`返回的结果与`a.view()`相同，否则返回的结果与`a.contiguous().view()`相同。

### 官方解释

- `reshape() `, `reshape_as()` and `flatten()` can return either a view or new tensor, user code shouldn't rely on whether it's view or not . 
- `contiguous()` returns itself if input tensor is already contiguous, otherwise it returns a new contiguous tensor by copying data .

## torch.Tensor.expand() & torch.Tensor.repeat()

### torch.Tensor.expand()

```python
torch.Tensor.expand(*sizes) → Tensor
```

将现有张量沿着值为1的维度扩展到新的维度。张量可以同时沿着任意一维或多维展开。

如果不想沿着一个特定的维度展开张量，可以设置它的参数值为-1。

```python
random_seed = 123
torch.manual_seed(random_seed)
# expand维度扩展
x = torch.Tensor([3, 2])
print(x)
print(x.size())
print(x.expand(3, 2), x.expand(3, 2).size())

x = torch.rand(3, 2)
print(x, x.shape)
print(x.expand(2, 3, 2), x.expand(2, 3, 2).size())

x = torch.rand(3, 1)
print(x, x.shape)
print(x.expand(2, 3, 2), x.expand(2, 3, 2).size())

a = torch.tensor([[[1, 2, 3], [4, 5, 6]]])
print(a)
print(a.size())
print(a.expand(3, 2, 3), a.expand(3, 2, 3).size())

'''输出结果'''
tensor([3., 2.]) torch.Size([2])
tensor([[3., 2.],
        [3., 2.],
        [3., 2.]]) torch.Size([3, 2])
tensor([[0.2961, 0.5166],
        [0.2517, 0.6886],
        [0.0740, 0.8665]]) torch.Size([3, 2])
tensor([[[0.2961, 0.5166],
         [0.2517, 0.6886],
         [0.0740, 0.8665]],

        [[0.2961, 0.5166],
         [0.2517, 0.6886],
         [0.0740, 0.8665]]]) torch.Size([2, 3, 2])
tensor([[0.1366],
        [0.1025],
        [0.1841]]) torch.Size([3, 1])
tensor([[[0.1366, 0.1366],
         [0.1025, 0.1025],
         [0.1841, 0.1841]],

        [[0.1366, 0.1366],
         [0.1025, 0.1025],
         [0.1841, 0.1841]]]) torch.Size([2, 3, 2])
tensor([[[1, 2, 3],
         [4, 5, 6]]]) torch.Size([1, 2, 3])
tensor([[[1, 2, 3],
         [4, 5, 6]],

        [[1, 2, 3],
         [4, 5, 6]],

        [[1, 2, 3],
         [4, 5, 6]]]) torch.Size([3, 2, 3])
```

### torch.Tensor.repeat()

```python
Tensor. repeat ( *sizes ) → Tensor
```

与`expand()`函数功能类似，两者的主要区别在于`expand()`函数张量**不会分配新的内存**，只是在存在的张量上创建一个新的视图（view），一个大小（size）等于1的维度扩展到更大的尺寸；`repeat()`函数将会拷贝张量的数据。

```python
a = torch.rand(1, 32, 1, 1)
print(a.repeat(4, 32, 1, 1).shape)
print(a.repeat(4, 1, 1, 1, 1).shape)

'''输出结果：'''
torch.Size([4, 1024, 1, 1])
torch.Size([4, 1, 32, 1, 1])
```



## torch.transpose() & torch.permute()

### torch.transpose()

```python
torch.transpose(input, dim0, dim1) → Tensor
```

 交换`dim0`和`dim1`的维度

```python
x = torch.rand(1, 2, 3, 4)
print(x, x.size())
a = x.transpose(1, 2)
print('交换1和2的维度：')
print(a, a.size())


'''输出结果'''
tensor([[[[0.4581, 0.4829, 0.3125, 0.6150],
          [0.2139, 0.4118, 0.6938, 0.9693],
          [0.6178, 0.3304, 0.5479, 0.4440]],

         [[0.7041, 0.5573, 0.6959, 0.9849],
          [0.2924, 0.4823, 0.6150, 0.4967],
          [0.4521, 0.0575, 0.0687, 0.0501]]]]) torch.Size([1, 2, 3, 4])
交换1和2的维度：
tensor([[[[0.4581, 0.4829, 0.3125, 0.6150],
          [0.7041, 0.5573, 0.6959, 0.9849]],

         [[0.2139, 0.4118, 0.6938, 0.9693],
          [0.2924, 0.4823, 0.6150, 0.4967]],

         [[0.6178, 0.3304, 0.5479, 0.4440],
          [0.4521, 0.0575, 0.0687, 0.0501]]]]) torch.Size([1, 3, 2, 4])
```

### torch.permute()

```python
torch.permute(input, dims) → Tensor
```

和`transpose()`函数功能相似，`transpose()`函数只能交换其中两个维度，`permute()`可以交换任意的维度。

```python
x = torch.rand(1, 2, 3, 4)
print(x, x.size())
a = x.permute(0, 3, 1, 2)
print('交换维度后：')
print(a, a.size())

'''输出结果：'''
tensor([[[[0.4581, 0.4829, 0.3125, 0.6150],
          [0.2139, 0.4118, 0.6938, 0.9693],
          [0.6178, 0.3304, 0.5479, 0.4440]],

         [[0.7041, 0.5573, 0.6959, 0.9849],
          [0.2924, 0.4823, 0.6150, 0.4967],
          [0.4521, 0.0575, 0.0687, 0.0501]]]]) torch.Size([1, 2, 3, 4])
交换维度后：
tensor([[[[0.4581, 0.2139, 0.6178],
          [0.7041, 0.2924, 0.4521]],

         [[0.4829, 0.4118, 0.3304],
          [0.5573, 0.4823, 0.0575]],

         [[0.3125, 0.6938, 0.5479],
          [0.6959, 0.6150, 0.0687]],

         [[0.6150, 0.9693, 0.4440],
          [0.9849, 0.4967, 0.0501]]]]) torch.Size([1, 4, 2, 3])
```

## 矩阵转置torch.Tensor.t()

```python
a = torch.rand(3, 4)
print(a)
print(a.t(), a.t().shape)

'''输出结果：'''
tensor([[0.4581, 0.4829, 0.3125, 0.6150],
        [0.2139, 0.4118, 0.6938, 0.9693],
        [0.6178, 0.3304, 0.5479, 0.4440]])
tensor([[0.4581, 0.2139, 0.6178],
        [0.4829, 0.4118, 0.3304],
        [0.3125, 0.6938, 0.5479],
        [0.6150, 0.9693, 0.4440]]) torch.Size([4, 3])
```

## torch.cat() & torch.stack()

### torch.cat()

```python
torch.cat(tensors, dim=0, *, out=None) → Tensor
```

在给定维中连接给定序列的seq张量。所有张量必须具有相同的形状（连接维度中除外）或为空。

可以将`torch.cat()`视为`torch.split()`和`torch.chunk()`的反向操作。

```python
# 张量拼接
x = torch.randn(2, 3)
print(x, x.size(0), x.size(1))
y = torch.cat((x, x, x), 0)     # 按行方向拼接
print(y, y.shape)
y1 = torch.cat((x, x, x), 1)    # 按列方向拼接
print(y1, y1.shape)
```

### torch.stack()

```
torch.cat(tensors, dim=0, *, out=None) → Tensor
```

`torch.stack()`是增加新的维度来完成拼接，不改变原维度上的数据大小。

```python
y = torch.rand(2, 3)
print(x)
print(y)
print('stack按行方向拼接：')
print(torch.stack((x, y), 0), torch.stack((x, y), 0).size())
print('cat按行方向拼接：')
print(torch.cat((x, y), 0), torch.cat((x, y), 0).size())
print('stack按列方向拼接：')
print(torch.stack((x, y), 1), torch.stack((x, y), 1).size())
print('cat按列方向拼接：')
print(torch.cat((x, y), 1), torch.cat((x, y), 1).size())


'''输出结果：'''
tensor([[-0.6014, -1.0122, -0.3023],
        [-1.2277,  0.9198, -0.3485]])
tensor([[0.7041, 0.5573, 0.6959],
        [0.9849, 0.2924, 0.4823]])
stack按行方向拼接：
tensor([[[-0.6014, -1.0122, -0.3023],
         [-1.2277,  0.9198, -0.3485]],

        [[ 0.7041,  0.5573,  0.6959],
         [ 0.9849,  0.2924,  0.4823]]]) torch.Size([2, 2, 3])
cat按行方向拼接：
tensor([[-0.6014, -1.0122, -0.3023],
        [-1.2277,  0.9198, -0.3485],
        [ 0.7041,  0.5573,  0.6959],
        [ 0.9849,  0.2924,  0.4823]]) torch.Size([4, 3])
stack按列方向拼接：
tensor([[[-0.6014, -1.0122, -0.3023],
         [ 0.7041,  0.5573,  0.6959]],

        [[-1.2277,  0.9198, -0.3485],
         [ 0.9849,  0.2924,  0.4823]]]) torch.Size([2, 2, 3])
cat按列方向拼接：
tensor([[-0.6014, -1.0122, -0.3023,  0.7041,  0.5573,  0.6959],
        [-1.2277,  0.9198, -0.3485,  0.9849,  0.2924,  0.4823]]) torch.Size([2, 6])
```

## torch.narrow()

```python
torch.Tensor.narrow(dimension, start, length) → Tensor
```

返回一个经过缩小后的张量。操作的维度由dimension指定。缩小范围是从start开始到start+length。执行本方法的张量与返回的张量共享相同的底层内存，返回的张量是原有张量的视图。

```python
x = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
m = x.narrow(0, 0, 2)  # 从行维度缩减，从0开始，缩小2的长度
print(m)
n = x.narrow(1, 1, 2)  # 从列维度缩减，从1开始，缩小2的长度
print(n)


'''输出结果：'''
tensor([[1., 2., 3.],
        [4., 5., 6.],
        [7., 8., 9.]])
tensor([[1., 2., 3.],
        [4., 5., 6.]])
tensor([[2., 3.],
        [5., 6.],
        [8., 9.]])
```

## split() & chunk()

### split()

```python
torch.split(tensor, split_size_or_sections, dim=0)
```

将tensor切分为多个块，每一块都是输入张量的视图

**参数：**

- tesnor：input带切分张量

- split_size_or_sections：需要切分的大小(int or list )

- dim：切分维度

- output：切分后块结构 <class 'tuple'>

```python
a = torch.arange(12).reshape(4,3)
print(a, a.shape)
# dim默认为0，对维度4进行split
# 当split_size_or_sections为int时，
# 如果dim与split_size_or_sections正好整除，则output正好匹配，
# 如果不能整除，则剩下的部分作为一个块处理
b = torch.split(a, 3)
for i in b:
    print(i, i.shape)
b = torch.split(a, [1, 3])
for i in b:
    print(i, i.shape)
# dim为1时，对维度3进行split
b = torch.split(a, 2, 1)
for i in b:
    print(i, i.shape)
b = torch.split(a, [1, 2], 1)
for i in b:
    print(i, i.shape)

'''输出结果：'''
tensor([[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11]]) torch.Size([4, 3])
tensor([[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]) torch.Size([3, 3])
tensor([[ 9, 10, 11]]) torch.Size([1, 3])
tensor([[0, 1, 2]]) torch.Size([1, 3])
tensor([[ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11]]) torch.Size([3, 3])
tensor([[ 0,  1],
        [ 3,  4],
        [ 6,  7],
        [ 9, 10]]) torch.Size([4, 2])
tensor([[ 2],
        [ 5],
        [ 8],
        [11]]) torch.Size([4, 1])
tensor([[0],
        [3],
        [6],
        [9]]) torch.Size([4, 1])
tensor([[ 1,  2],
        [ 4,  5],
        [ 7,  8],
        [10, 11]]) torch.Size([4, 2])
```

### chunk

将张量拆分为指定个数的块。 每个块都是输入张量的视图。

如果给定维度dim上的张量大小可被chunk个数整除，则所有返回的块大小都相同。如果给定维度dim上的张量大小不能被chunk个数整除，则所有返回的块大小都将相同，最后一个除外。如果无法进行这种划分，则此函数返回的块数可能小于指定的块数。

**参数：**

- **input** (Tensor) – 待切分的张量
- **chunks** (int) – 需要返回的chunk个数
- **dim** (int) – 需要沿着切分的维度

```python
print(torch.arange(11).chunk(6))
print(torch.arange(12).chunk(6))
print(torch.arange(13).chunk(6))

'''输出结果：'''
(tensor([0, 1]), tensor([2, 3]), tensor([4, 5]), tensor([6, 7]), tensor([8, 9]), tensor([10]))
(tensor([0, 1]), tensor([2, 3]), tensor([4, 5]), tensor([6, 7]), tensor([8, 9]), tensor([10, 11]))
(tensor([0, 1, 2]), tensor([3, 4, 5]), tensor([6, 7, 8]), tensor([ 9, 10, 11]), tensor([12]))
```



## pytorch的tensor与numpy的NDArray转换

### tensor -> NDArray

```python
x = torch.rand(2, 3)
print(x)
ndarray = x.numpy()  # x本身就是tensor,直接调用numpy()函数
print(ndarray)

'''输出结果：'''
tensor([[0.4581, 0.4829, 0.3125],
        [0.6150, 0.2139, 0.4118]])
[[0.45808464 0.48285657 0.31249833]
 [0.61502165 0.2139473  0.4118262 ]]
```

### NDArray -> tensor

```python
ndarray1 = np.random.randn(2, 3)
print(ndarray1)
x1 = torch.from_numpy(ndarray1)  # 要使用torch.from_numpy()
print(x1)

'''输出结果：'''
[[-0.10561537  1.17134399  0.52127628]
 [-0.34410791  0.42745323 -0.25840794]]
tensor([[-0.1056,  1.1713,  0.5213],
        [-0.3441,  0.4275, -0.2584]], dtype=torch.float64)
```

## 掩码索引masked_select

根据mask进行取值

```python
x = torch.randn(3, 4)
print(x)
mask = x.ge(0.5)  # greater equal大于等于
print(mask)
y = torch.masked_select(x, mask)
print(y)

'''输出结果：'''
tensor([[-0.6014, -1.0122, -0.3023, -1.2277],
        [ 0.9198, -0.3485, -0.8692, -0.9582],
        [-1.1920,  1.9050, -0.9373, -0.8465]])
tensor([[False, False, False, False],
        [ True, False, False, False],
        [False,  True, False, False]])
tensor([0.9198, 1.9050])
```

## 查看Tensor的运行设备

```python
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.device_count())
print(torch.cuda.get_device_name())
print(torch.cuda.is_available())

x = torch.randn(2, 3)
y = torch.randn(3, 2)
x, y = x.to(device='cuda'), y.to(device='cuda')  # 将数据转到GPU上
xy = torch.mm(x, y)
print(xy)
x, y = x.to(device='cpu'), y.to(device='cpu')  # 将数据转到CPU上
xy = torch.mm(x, y)
print(xy)

'''输出结果：'''
0
<torch.cuda.device object at 0x7fbb04c8b1d0>
1
Tesla V100-SXM2-32GB
True

tensor([[0.9019, 1.2118],
        [2.0397, 0.3485]], device='cuda:0')
tensor([[0.9019, 1.2118],
        [2.0397, 0.3485]])
```

