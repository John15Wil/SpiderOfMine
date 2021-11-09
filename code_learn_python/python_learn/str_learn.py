'''
获取长度:len len函数可以获取字符串的长度。
查找内容:find 查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次 出现的开始位置索引值，如果不存在，则返回-1.
判断:startswith,endswith 判断字符串是不是以谁谁谁开头/结尾
计算出现次数:count 返回 str在start和end之间 在 mystr里面出现的次数
替换内容:replace 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
切割字符串:split 通过参数的内容切割字符串 修改大小写:
upper,lower 将字符串中的大小写互换 空格处理:
strip 去空格 字符串拼接:
join 字符串拼接
'''

a = "hello world   "
b = "nihao"
res1 = len(a)
res2 = a.find("e")
res3 = a.startswith("w")
# split = a.split("l")
# for s in split:
#     print(s.upper())

print(res1)
print(res2)
print(res3)
res4 = a.strip()
print(res4)
res5=a.join(b)
print(res5)