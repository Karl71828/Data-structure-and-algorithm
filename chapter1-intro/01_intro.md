## 1.1 算法效率衡量

### 1.1.1 时间复杂度
每台机器执行的总能够时间不同，
但执行基本运算的数量大体相同。

**时间复杂度与大O记法**
    
        往往并不用分析的那么细致，大概看一下数量级
    
        n:与问题的规模有关

**最坏时间复杂度**


```
    最坏时间复杂度：保证 下限
    最优时间复杂度：没什么有用的信息
```

**时间复杂度的计算规则**
1. 基本操作，只有常数项 认为是O(1)
2. 顺序结构：加法
3. 循环结构：乘法
4. 分支结构：取最大值的那路
5. 判断一个算法效率时，只需要关注最高次项
6. 没有特殊说明话，分析的复杂度 都是指的最坏时间复杂度

**常见的时间复杂度**

==大小关系！！==

O(1) < O(logn) < O(n)

< O(nlogn) < O(n^2) <O (n^3)

< O(2^n) < O(n!) < O(n^n)


**代码执行时间测量**


```python
class timeit.Timer( # Timer是测量小段代码执行速度的类
    stmt='pass',  # stmt参数是要测试的代码语句（statment）
    setup='pass',  # setup参数是运行代码时需要的设置
    timer=<timer function> # timer参数是一个定时器函数，与平台有关
)
```

**list操作测试**


```python
见"02_list.py"
```


```
pop从头部取出 也比 从尾部取出 慢得多

list\dict并不是基本数据类型
```

## 1.2 数据结构的引入

算法：一种思想、解题步骤

数据结构：怎么把数据组织在一起


```python
# 存储学生信息

# 列表
[
    ("ZhangSan",20,"jiangsu"),
    ("ZhangSan",20,"jiangsu"),
    ("ZhangSan",20,"jiangsu"),
]

for stu in stus:
    if stu[0] == "ZhangSan":

# 字典 键值对
[
    {
        "name": "ZhangSan",
        "age": 20,
        "hometown": jiangsu
    },
]

[
    "ZhangSan":{
        "age": 20,
        "hometown": jiangsu
    },
]
stus["ZhangSan"]

```


程序 = 数据结构 + 算法

**抽象数据类型**
有面向对象的意思了