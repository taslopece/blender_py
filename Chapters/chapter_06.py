# function
# 函数

def main():
    name_of_print("Hello World!")
    print(sum(1, 2))

    range_nums = [random.randint(0, 10) for n in range(10)]
    print(range_nums)


def name_of_print(string):
    print(string)
# def name_of_print(*args):
#     for arg in args:
#         print(arg)



# lambda
# 匿名函数
sum = lambda n1,n2 : n1 + n2
# print(sum(1,2))


# import
# 导入
## 导入标准库中的方法

import random

# range_nums = [random.randint(0,10) for n in range(10)]
# print(range_nums)

if __name__ == '__main__':
    main()