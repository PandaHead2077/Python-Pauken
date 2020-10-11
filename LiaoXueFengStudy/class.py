# class
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，
# 继承的概念我们后面再讲，通常，如果没有合适的继承类，
# 就使用object类，这是所有类最终都会继承的类。

class student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
    
bart = student('Bart Simpson',99)
bart.print_score()


#访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class student(object):
    def __init__(self, name, gender):
            self.__name = name
            self.__gender = gender
    
    def set_gender(self, setgender):
        if setgender not in ['female','male']:
            raise ValueError('Wrong Input')
        else:
            self.__gender = setgender
    
    def print_gender(self):
        print(self.__gender)
            
ss = student(23,'female')
ss.print_gender()
ss.set_gender('male')
ss.print_gender()
            
#####继承和多态
#子类的run()覆盖了父类的run()
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
#isinstance(c, Animal)
#动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

####获取对象信息

