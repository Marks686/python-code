# 函数中三大结构和嵌套调用时的执行过程
# def demo1():
#     print(1)
#     print(2)
#     print(3)

# def demo2():
#     print(1)
#     if True:
#         print(2)
#     print(3)

# def demo3():
#     print(1)
#     for i in range(3):
#         print(2)
#     print(3)

def demo4_a():
    print("a_start")
    print("a_stop")

def demo4_b():
    print("b_start")
    demo4_a()
    print("b_stop")

demo4_b()
print(100)
