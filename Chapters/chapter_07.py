# 异常处理

# list1 = []
#
# try:
#     print(list1[1])
#
# except(Exception) as e:
#     print(f"出现错误\n{e}")
# finally:
#     print("Please check your code")

# class
# 类

class Object():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(f"Object name is {self.name}")

    @staticmethod
    def print__(obj):
        print("this is static method")
        print(obj)

# cube = Object(name="myCube")
# print(type(cube))
