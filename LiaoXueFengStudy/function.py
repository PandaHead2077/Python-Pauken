# function
help(abs)

n1 = 255
n1 = hex(n1)
print(n1)

#function's name
a = abs
print(a(-25))

#empty function
def nop():
    pass
    
#参数检查
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
        
#返回多个值
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

import math
print(math.sqrt(2))


#默认参数
# def power(x,n=2):

#必选参数在前，默认参数在后
#定义默认参数要牢记一点：默认参数必须指向不变对象！

#为什么要设计str、None这样的不变对象呢？
#因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

#可变参数
#定义
#   def calc(*numbers):
#调用函数：
#   nums = [1, 2, 3]
#   calc(*nums)

#关键字参数
#定义：
#   def person(name, age, **kw):
#调用函数：
#   extra = {'city': 'Beijing', 'job': 'Engineer'}
#   person('Jack', 24, **extra)

    # 命名关键字参数
    #def person(name, age, *, city, job):
        #如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
        #def person(name, age, *args, city, job):
    #命名关键字参数必须传入参数名，这和位置参数不同。   
    #def person(name, age, *, city='Beijing', job):
  
###参数组合###
#必选参数、默认参数、可变参数、关键字参数和命名关键字参数
#顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。











































