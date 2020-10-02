#模块！
from test import test1
s=haha(2)
print(s)


#mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
 
 
#文件www.py的模块名就是mycompany.web.www，
# 两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。

# 使用模块
# 任何模块代码的第一个字符串都被视为模块的文档注释；
#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
