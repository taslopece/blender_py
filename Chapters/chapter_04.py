# List
# 列表以及列表的增删查改

list1 = [1, 2, 3, 4, 5]

list2 = []
a = 'element a'

list2.append(a)
print(list2)


# 增
print("list的增")

for i in list1:
    print(i)
    new = str(i)
    list2.append(new)

print(list2)
list3 = list2 + list1
print(list3)

# 删
print("list的删")

print(list2)
list2.pop()
print(list2)

list3.remove("4")
print(list3)


# 查

# 改

list4 = list3[:-2]
print(list4)
