# 定义一个元组
info_data = (1, "张三", 1.45)
print(info_data)
print(type(info_data))
info_data_1 = (1)
print(type(info_data_1))
info_data_2 = (1,)
print(type(info_data_2))

# 统计元组中出现的元素
info_data_3 = (1, 2, 3, 1, 1, 3, 2)
print(info_data_3.count(1))

# index 指当前元素的下标
print(info_data_3.index(3))

for i in info_data_3:
    print(i)

print(type(list(info_data_3)))
print(info_data_3)