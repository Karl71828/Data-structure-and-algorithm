# coding utf-8

# 四种生成列表的方法
# li1 = [1,2]
# li2 = [11,12]
# li = li1+li2
#
# li = [i for i in range(10000)]
#
# li = list(range(10000))
#
# li = []
# for i in range(10000):
#     li.append(i)



def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)     # 从尾部添加


def test3():
    l = [i for i in range(1000)]


def test4():
        l = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
#            字符串         设置：导入test1
print("concat ", t1.timeit(number=1000), "seconds")
#                t1.timeit(1000)
#  测1000次 求平均值；timeit有返回值的 单位是s

t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "seconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "seconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "seconds")


def test5():
    l = []
    for i in range(1000):
        l.insert(0,i)   # 从头部添加

t5 = Timer("test5()", "from __main__ import test5")
print("insert ", t5.timeit(number=1000), "seconds")


#   concat  1.1558527 seconds
#   append  0.05823559999999994 seconds
#   comprehension  0.027968699999999957 seconds
#   list range  0.010738600000000043 seconds
#   insert  0.2353368 seconds

