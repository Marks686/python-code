class Hero:
    def __init__(self,name,sex,hp,attack):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.attack = attack
    def info(self):
        print("我是一个英雄")

anqila = Hero("anqila","女",1000,500)
chengyaojin = Hero("chengyaojin","男",8000,200)
print(anqila.name)
print(anqila.sex)
print(anqila.hp)
print(anqila.attack)
print(chengyaojin.name)