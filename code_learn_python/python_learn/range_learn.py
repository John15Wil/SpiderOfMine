'''
append 在末尾添加元素
insert 在指定位置插入元素
extend 合并两个列表
'''

A = ['xiaoWang','xiaoZhang','xiaoHua']
A.append("nihao")
A.insert(3,"hello")
B= ['1','2','5']
A.extend(B)

A[1]='xiaoli'

if "xiaolia" not in A:
    print("随便输出不在一下")
# A.remove("xiaoli")
print(A)
A.pop(3)
print(A)
A.pop()
print(A)
del A[2]
print(A)
print(A[1][1:3])


# 字典
info={'name':"zhangsan",'age':"12"}
get = info.get('name')
print(get)
