#Dictionary
#字典及字典的增删查改

list1 = [1, 3, 4, 4, 5, 6]

list2 = list(set(list1))
print(list2)

dict1 = {"gender":"male", "age":18, "name":"Robert"}
print(dict1["gender"])

# 增
dict1["height"] = 1.80
print(dict1)

# 删
del dict1["gender"]
print(dict1)

# 查

# 改
## 直接键值对赋值

# 遍历
for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for k,v in dict1.items():
    print(k,v)

# list to dictionary
# 列表到字典

list3 = [1, 10, 10, 8, 2, 5, 4]
list4 = [str(i) for i in list3]

print(list3)
print(list4)

dict2 = dict(zip(list3, list4))
print(dict2)

