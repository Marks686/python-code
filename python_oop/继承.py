class A:
    money = 20
    def study(self):
        print("学的好")

class B(A):
    name = "likaixuan"
    def sleep(self):
        print("睡得好")


print(A.money)
print(B.money)

b = B()
b.study()