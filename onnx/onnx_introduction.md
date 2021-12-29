---
title: onnx_introduction
date: 2021-10-11 18:28:16
tags:
- onnx
- 推理优化
categories: 
- onnx

---

## 简介

[ONNX](https://github.com/onnx/onnx)（Open Neural Network Exchange）- 开放神经网络交换格式，作为框架公用的一种模型交换格式，使用protobuf二进制格式来序列化模型。onnx兼容大多数的深度学习框架，在训练完成之后可以将这些框架得到的模型统一存储为onnx这种同一个格式进行存储。onnx文件不仅仅存储了神经网络模型的权重，同时也存储了模型的结构信息以及网络中每一层的输入输出和一些其它的辅助信息。在得到onnx模型之后还可以进而转换成不同部署框架所需要的类型，例如：

- Pytorch -> onnx -> TensorRT
- Pytorch -> onnx -> TensorFlow
- Pytorch -> onnx -> onnxruntime

<!--more-->

## 1. 使用torch.onnx加载模型到onnx

[torch.onnx官方文档与教程](https://pytorch.org/docs/master/onnx.html)

Pytorch模型定义和模型权重暂时不支持打包在一起，这在推理时候需要先用模型定义代码构建模型，再加载模型权重。借助于onnx格式转换可以把模型打包一起，在ONNX Runtime中运行推理，[ONNX Runtime](https://github.com/microsoft/onnxruntime) 是针对 ONNX 模型的以性能为中心的引擎，可大大提升模型的性能。另外，onnx模型支持在不同框架之间转换，也支持tensorRT加速。

### 加载pytorch模型

首先将Pytorch模型加载进来，包括模型结构定义和权重加载。注意需要将模型转换成推理模式，去除dropout和batchnorm层训练和推理不同的影响。

```python
torch_model = model()
torch_model.load_state_dict()

# set the model to inference mode
torch_model.eval()
```

### pytorch模型转换成onnx格式

调用`torch.onnx.export()`函数将Pytorch模型转换成ONNX格式。 这将执行模型，并记录使用什么运算符计算输出的轨迹。 因为`export`运行模型，所以需要提供输入张量`x`。由于pytorch在不断更新来解决转onnx过程中的bug，建议采用opset_version=11，onnx对一些层支持性较好。

```python
# Input to the model
x = torch.randn(batch_size, 1, 224, 224, requires_grad=True)
torch_out = torch_model(x)
# Export the model
torch.onnx.export(torch_model,                       
                  x,                                 # model input (or a tuple for multiple inputs)
                  "test.onnx",                       # where to save the model (can be a file or file-like object)
                  export_params=True,                # 存储模型时同时导出所有参数，如果导入未经训练模型，设置为False
                  opset_version=11,                  # the ONNX version to export the model to
                  do_constant_folding=True,          # 如果为 True，则在导出期间将恒定折叠优化应用于模型。 常量折叠优化将用预先计算的常量节点替换一些具有所有常量输入的操作。
                  input_names = ['input'],           # the model's input names
                  output_names = ['output'],         # the model's output names
                  dynamic_axes={'input' : {0 : 'batch_size'},       # variable lenght axes
                                'output' : {0 : 'batch_size'}})
```

### onnx模型精度验证

```python
import onnx
onnx_model = onnx.load("test.onnx")
onnx.checker.check_model(onnx_model)

import onnxruntime
ort_session = onnxruntime.InferenceSession("test.onnx")
def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()
ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(x)}
ort_outs = ort_session.run(None, ort_inputs)

# compare ONNX Runtime and PyTorch results
np.testing.assert_allclose(to_numpy(torch_out), ort_outs[0], rtol=1e-03, atol=1e-05)
print("Exported model has been tested with ONNXRuntime, and the result looks good!")


# check the output against PyTorch
onnx_out = onnx_model(x)
print(torch.max(torch.abs(torch_out - onnx_out)))
```

### onnx模型使用onnxruntime推理

使用 ONNX Runtime 运行模型，需要使用onnxruntime.InferenceSession("test.onnx")为模型创建一个推理会话。创建会话后，我们将使用 run(）API 运行推理模型获得推理输出结果。这样，就完成了Pytorch模型的打包推理。

```python
from PIL import Image
import torchvision.transforms as transforms

img = Image.open("./_static/img/cat.jpg")
image = np.asarray(img ,dtype=np.float32)
image = np.transpose(image,(2,0,1))##input in CHW format

ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(x)}
ort_outs = ort_session.run(None, ort_inputs)
```

## 2. 使用huggingface加载pytorch模型到onnx

本质上huggingface也是调用了torch.onnx.export函数

```python
from pathlib import Path
from transformers.convert_graph_to_onnx import convert
 
# Handles all the above steps for you
convert(framework="pt", model="/home/data/pretrain_models/bert-base-chinese-pytorch", output=Path("onnx/bert-base-chinese.onnx"), opset=11)
# 注意：因为convert_graph_to_onnx.convert中默认的pipeline_name是"feature-extraction"。如果是其他任务，则需要对应修改。具体支持哪些pipeline_name可以在官方接口中查阅。
```

## onnx模型优化

通过使用特定的后端来进行inference，后端将启动特定硬件的graph优化。有3种基本的优化：

- Constant Folding: 将graph中的静态变量转换为常量

- Deadcode Elimination: 去除graph中未使用的nodes

- Operator Fusing: 将多条指令合并为一条(比如，Linear -> ReLU 可以合并为 LinearReLU)

在ONNX Runtime中通过设置特定的SessionOptions会自动使用大多数优化。一些尚未集成到ONNX Runtime 中的最新优化可在优化脚本中找到，利用这些脚本可以对模型进行优化以获得最佳性能。

优化工具包：onnxruntime-tools

```python
# optimize transformer-based models with onnxruntime-tools
 
from onnxruntime_tools import optimizer
from onnxruntime_tools.transformers.onnx_model_bert import BertOptimizationOptions
 
# disable embedding layer norm optimization for better model size reduction
opt_options = BertOptimizationOptions('bert')
opt_options.enable_embed_layer_norm = False
 
opt_model = optimizer.optimize_model(
    'onnx/bert-base-chinese.onnx',
    'bert', 
    num_heads=12,
    hidden_size=768,
    optimization_options=opt_options)
opt_model.save_model_to_file('onnx/bert-base-chinese.opt.onnx')
```

优化后的graph可能包括各种优化，如果想要查看优化后graph中一些更高层次的操作(例如EmbedLayerNormalization、Attention、FastGeLU)可以通过比如[Netron](https://netron.app/)等可视化工具查看。

加载ONNX模型进行inference。

```python
from os import environ
from psutil import cpu_count
 
# Constants from the performance optimization available in onnxruntime
# It needs to be done before importing onnxruntime
environ["OMP_NUM_THREADS"] = str(cpu_count(logical=True)) # OMP 的线程数
environ["OMP_WAIT_POLICY"] = 'ACTIVE'
# 以上代码开启OpenMP加速
 
from onnxruntime import GraphOptimizationLevel, InferenceSession, SessionOptions, get_all_providers
 
from contextlib import contextmanager
from dataclasses import dataclass
from time import time
from tqdm import trange
 
def create_model_for_provider(model_path: str, provider: str) -> InferenceSession: 
  
  assert provider in get_all_providers(), f"provider {provider} not found, {get_all_providers()}"
 
  # Few properties that might have an impact on performances (provided by MS)
  options = SessionOptions()
  options.intra_op_num_threads = 1
  options.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
 
  # Load the model as a graph and prepare the CPU backend 
  session = InferenceSession(model_path, options, providers=[provider])
  session.disable_fallback()
    
  return session
 
 
@contextmanager
def track_infer_time(buffer: [int]):
    start = time()
    yield
    end = time()
 
    buffer.append(end - start)
 
 
@dataclass
class OnnxInferenceResult:
  model_inference_time: [int]  
  optimized_model_path: str
```

在CPU上加载ONNX模型，并进行推理：

```python
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained("/home/data/pretrain_models/bert-base-chinese-pytorch") # 使用 Pytorch 模型的字典
cpu_model = create_model_for_provider("onnx/bert-base-chinese.opt.onnx", "CPUExecutionProvider") # 使用 优化过的 onnx

# Inputs are provided through numpy array
model_inputs = tokenizer("大家好, 我是卖切糕的小男孩, 毕业于华中科技大学", return_tensors="pt")
inputs_onnx = {k: v.cpu().detach().numpy() for k, v in model_inputs.items()}

# Run the model (None = get all the outputs)

sequence, pooled = cpu_model.run(None, inputs_onnx)

# Print information about outputs

print(f"Sequence output: {sequence.shape}, Pooled output: {pooled.shape}")
```

在cpu上运行pytorch模型（baseline）

```python
from transformers import BertModel
 
PROVIDERS = {
    ("cpu", "PyTorch CPU"),
#  Uncomment this line to enable GPU benchmarking
#    ("cuda:0", "PyTorch GPU")
}
 
results = {}
 
for device, label in PROVIDERS:
    
    # Move inputs to the correct device
    model_inputs_on_device = {
        arg_name: tensor.to(device)
        for arg_name, tensor in model_inputs.items()
    }
 
    # Add PyTorch to the providers
    model_pt = BertModel.from_pretrained("/home/data/pretrain_models/bert-base-chinese-pytorch").to(device)
    for _ in trange(10, desc="Warming up"):
      model_pt(**model_inputs_on_device)
 
    # Compute 
    time_buffer = []
    for _ in trange(100, desc=f"Tracking inference time on PyTorch"):
      with track_infer_time(time_buffer):
        model_pt(**model_inputs_on_device)
 
    # Store the result
    results[label] = OnnxInferenceResult(
        time_buffer, 
        None
    )
```

在cpu上运行onnx模型

```python
PROVIDERS = {
    ("CPUExecutionProvider", "ONNX CPU"),
#  Uncomment this line to enable GPU benchmarking
#     ("CUDAExecutionProvider", "ONNX GPU")
}
 
# ONNX
for provider, label in PROVIDERS:
    # Create the model with the specified provider
    model = create_model_for_provider(model_onnx_path, provider)
 
    # Keep track of the inference time
    time_buffer = []
 
    # Warm up the model
    model.run(None, inputs_onnx)
 
    # Compute
    for _ in trange(100, desc=f"Tracking inference time on {provider}"):
      with track_infer_time(time_buffer):
          model.run(None, inputs_onnx)
 
    # Store the result
    results[label] = OnnxInferenceResult(
      time_buffer,
      model.get_session_options().optimized_model_filepath
    )
 
 
# ONNX opt
 
PROVIDERS_OPT = {
    ("CPUExecutionProvider", "ONNX opt CPU")
}
 
for provider, label in PROVIDERS_OPT:
    # Create the model with the specified provider
    model = create_model_for_provider(model_opt_path, provider)
 
    # Keep track of the inference time
    time_buffer = []
 
    # Warm up the model
    model.run(None, inputs_onnx)
 
    # Compute
    for _ in trange(100, desc=f"Tracking inference time on {provider}"):
      with track_infer_time(time_buffer):
          model.run(None, inputs_onnx)
 
    # Store the result
    results[label] = OnnxInferenceResult(
      time_buffer,
      model.get_session_options().optimized_model_filepath
    )
 
# 将 result save 处理, 绘制结果对比图
import pickle
with open('results.pkl', 'wb') as f:
    pickle.dump(results, f, pickle.HIGHEST_PROTOCOL)
```

Pytorch模型量化

```python
import torch 
from transformers import BertTokenizerFast

# Load Pytorch model
torch_model = "/home/data/pretrain_models/bert-base-chinese-pytorch"
model_pt = BertModel.from_pretrained("/home/data/pretrain_models/bert-base-chinese-pytorch").to(device)

tokenizer = BertTokenizerFast.from_pretrained(torch_model)

# Quantize
model_pt_quantized = torch.quantization.quantize_dynamic(
    model_pt.to("cpu"), {torch.nn.Linear}, dtype=torch.qint8
)

model_inputs = tokenizer("大家好, 我是卖切糕的小男孩, 毕业于华中科技大学", return_tensors="pt")

# Warm up 
model_pt_quantized(**model_inputs)

# Benchmark PyTorch quantized model
time_buffer = []
for _ in trange(100):
    with track_infer_time(time_buffer):
        model_pt_quantized(**model_inputs)
    
results["PyTorch CPU Quantized"] = OnnxInferenceResult(
    time_buffer,
    None
)

```

onnx模型量化

```python
## ONNX Quantize
from transformers.convert_graph_to_onnx import quantize
onnx_quantized_model_path = quantize(Path(model_onnx_path))
quantized_model = create_model_for_provider(onnx_quantized_model_path.as_posix(), "CPUExecutionProvider")

# Warm up the overall model to have a fair comparaison
outputs = quantized_model.run(None, inputs_onnx)

# Evaluate performances
time_buffer = []
for _ in trange(100, desc=f"Tracking inference time on CPUExecutionProvider with quantized model"):
    with track_infer_time(time_buffer):
        outputs = quantized_model.run(None, inputs_onnx)

# Store the result
results["ONNX CPU Quantized"] = OnnxInferenceResult(
    time_buffer,
    onnx_quantized_model_path
)

```

