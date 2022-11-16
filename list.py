name_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
name_list.insert(0, 0);
print(name_list)
list2 = ["adsfasdf", "chenhuajian"]
# 链接另一个列表数据
name_list.extend(list2)
print(name_list)

# 删掉指定数据
del name_list[len(name_list) - 1]
print(name_list)

# 删除一个第一次出现的数据
print("删除一个第一次出现的数据")
name_list.append(0)
name_list.remove(0)
print(name_list)
print("------------------------")
# pop删除
print(name_list.pop())
print(name_list)

# pop 索引删除
print(name_list.pop(0))
print(name_list)

# 清楚整个列表
# name_list.clear()
# print(name_list)

# 统计列表索引
print(len(name_list))

# 统计列表中元素出现的次数
name_list.append(8)
print(name_list.count(8))

another_list = name_list
another_list[0] = 999
print(name_list)

# 列表排序
new_list = [1, 2, 0, 3, 8, 9, 1, 5, 6, 87, 2, 36, 47]
new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
new_list.reverse()
print(new_list)

# 循环输出
for i in new_list:
    print(i)
    print(type(i))