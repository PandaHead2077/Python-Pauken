# list 
# 最后一个元素索引
s = [1,2,3,4,5,6,7,8,9]
print(s[-1])
print(s[-3])
print(s[0])
# add element
s.append('Adam')
print(s)

s.insert(3,'ao')
print(s)
# delete last element
s.pop()
print(s)

s.pop(-2)
print(s)

#subsititute element
s[-3]='sus'
print(s)

# tuple 现在这个tuple不能变了，它也没有append()，insert()这样的方法
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

t=(1,2,3,'woc')
print(t)
# 避免小括号歧义
tp = (1,)
print(tp)

#tuple的元素不可变，tuple元素的元素可变————指向问题
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
print(t)

