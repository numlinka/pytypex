# pytypex

_Python fundamental type extension_\
_Python 基础类型扩展_

Implement types not provided by the standard library, such as static classes,
singleton classes, and atomic counters.\
实现标准库未提供的类型，例如静态类、单例类和原子计数器。

The preferred way to install typex is via pip.\
安装 typex 的首选方法是通过 pip。

```shell
pip install typex
```

To upgrade logop to the latest version, use the following command.\
要将 typex 升级到最新版本，请使用以下命令。

```shell
pip install --upgrade typex
```

Here are a few simple usage examples.\
以下是一些简单的使用示例。

```Python
# Static class
from typex import Static

class MyStatic (Static):
    my_static_var = 0

MyStatic()  # raise TypeError
```

```Python
# Singleton class
from typex import Singleton

class MySingleton (Singleton):
    def __init__(self):
        print("MySingleton is initialized")

a = MySingleton()  # MySingleton is initialized
b = MySingleton()  # (Nothing)
c = MySingleton()  # (Nothing)

print(a is b)  # True
```

```Python
# Multiton class
from typex import Multiton

class MyMultiton (Multiton):
    def __init__(self, value):
        print(value)

a1 = MyMultiton(1)  # 1
a2 = MyMultiton(2)  # (Nothing)
b1 = MyMultiton.get_instance("new", 3)  # 3
b2 = MyMultiton(4, instance_name="new")  # (Nothing)

print(a1 is a2)  # True
print(b1 is b2)  # True
print(a1 is b1)  # False

print(a1.instance_name)  # default
print(b1.instance_name)  # new

# For instances that have already executed the __init__ method,
# you do not need to pass value.
a3 = MyMultiton()  # (Nothing)
print(a3.instance_name)  # default
```

```Python
# Atomic counter
from typex import Atomic, AbsoluteAtomic, MultitonAtomic

a = AbsoluteAtomic()
for _ in range(4): print(a.value)  # 0 1 2 3

b = AbsoluteAtomic()
for _ in range(4): print(b.count)  # 4 5 6 7

c = AbsoluteAtomic()
for _ in range(4): print(c.value)  # 8 9 10 11

d = Atomic()
for _ in range(4): print(d.count)  # 12 13 14 15

# I'm too lazy to demonstrate, you just need to know that it has the
# characteristics of both Multiton and Atomic.
MultitonAtomic()
```

---

This project is licensed under the MIT License.\
该项目使用 MIT 许可证授权。

pytypex Copyright (C) 2022 numlinka.
