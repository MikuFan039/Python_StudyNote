s='HelloWorld'
# 切片操作
s1=s[0:5:2] # 索引从0开始，到5结束（不包含5）步长为2
print(s1)
# 省略了开始位置 ，start默认从0开始
print(s[:5:1])
# 省略开始位置start，省略不步长step
print(s[:5:])
# 省略结束位置
print(s[0::1]) # stop，默认到序列的最后一个元素（包含最后一个元素)

print(s[5::])
print(s[5:]) # 12行代码与13行代码功能相同，省略了结束，省略了一个步长
# 更改一下步长，步长更改为2
print(s[0:5:2])

# 省略开始位置 ，省略结束位置 ，只写步长
print(s[::2]) # 分别获取0，2，4，6，8索引位置 上的元素

# 步长为负数
print(s[::-1]) # 可以使用哪句代码替换呢
print(s[-1:-11:-1]) 
