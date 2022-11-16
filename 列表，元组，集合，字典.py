# args = [3, 6]
# #用 * 对列表进行解包
# print(range(*args))
# print(list(range(*args)))
#
# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# print(knights.items())

# squares = [x ** 2 for x in range(10)]
# print(squares)
# # 列表推导式
# squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(squares)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# 为嵌套


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# print([[row[i] for row in matrix] for i in range(4)])
# # 用 * 对matrix进行解包
# # 用 zip 进行元组装换， 即将函数内每个迭代器的第i个进行元组组合 !!!python3.7不支持该关键字 可用strict=Ture 来判断zip内的迭代器是否长度相同
# print(list(zip(*matrix)))


# 集合推导式
# collection = {x for x in 'asdgfdsxcvvafdgrwerqwefasdgtyw' if x not in 'ac'}
# print(collection)

# # 字典推导式
# dictionary = {x: x ** 2 for x in (2, 4, 6)}
# print(dictionary)

# # dict(sape=4139, guido=4127, jack=4098)
# # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# # 用 items() 方法可同时取出键和对应的值：
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# # 用 enumerate() 函数可以同时取出位置索引和对应的值
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# 互异性
# self = {1, 2, 3, 3, 2}
# # {1, 2, 3}
# print(self)


# # 成员运算
# print(10 in {1, 2, 3, 10, 2, 4, 5})
# print(10 not in {1, 2, 3, 10, 2, 4, 5})

# # 交集运算
# col_1 = {1, 2, 3}
# col_2 = {2, 4, 5}
# print(col_1 & col_2)
# print(col_1.intersection(col_2))

# # 并集运算
# col_3 = {2, 3, 4}
# col_4 = {3, 10, 20, 30}
# print(col_3 | col_4)
# print(col_3.union(col_4))

# # 差集运算
# col_5 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# col_6 = {2, 4, 6, 8, 10}
# print(col_6 - col_5)
# # {10}
# print(col_5 - col_6)
# print(col_5.difference(col_6))

# # 对称差
# col_7 = {1, 2, 3, 4, 5, 6, 8, 9}
# col_8 = {2, 3, 4, 5, 7, 10}
# print(col_8 ^ col_7)
# print(col_7 ^ col_8)
# print(col_7.symmetric_difference(col_8))
# print((col_7 | col_8) - (col_7 & col_8))


# # 比较运算符
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = set2
# # < 为真子集 <= 为子集
# print(set1 < set2, set1 <= set2)
# # issubset(x) 判断当前集合是否为x的子集
# print(set1.issubset(set2))
# print(set3 < set2, set3 <= set2)
#
# # > 为超集
# print(set2 > set1, set2 > set3)
# # issupperset(x) 判断当前集合是否为x的超集
# print(set2.issuperset(set1))

# set_1 = set()
# set_1.add(33)
# set_1.add(55)
# # set_1 {33, 55}
# set_1.update({1, 2, 3, 10, 50, 100, 30, 1000})
# print(set_1)

_set1 = {1, 2, 3, 4, 10, 100, 200, 1000, 5}
_set1.discard(5)
print(_set1)
# 此函数删除不存在的元素时不会报错
_set1.discard(5)
print(_set1)

try:
    _set1.remove(5)
except:
    print("error")
else:
    print("allow")