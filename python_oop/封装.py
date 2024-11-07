class Hero:

    __born_position = "泉水"
    def __init__(self,name,sex,hp,attack):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.attack = attack
    def info(self):
        print("我叫{},性别{},血量{},攻击力{},英雄出生在{}".format(self.name,self.sex,self.hp,self.attack,Hero.born_position))

    @classmethod
    def where_was_i_born(cls):
        print("我在{}出生".format(cls.born_position))

    @classmethod
    def get_born_position(cls):
        return cls.__born_position

    @classmethod
    def set_born_position(cls,x):
        cls.__born_position = x
        return cls.__born_position

# Hero.where_was_i_born(
# anqila = Hero("anqila","女",1000,500)
# anqila.info()

# Hero.born_position = "龙坑"

print(Hero.get_born_position())
Hero.set_born_position("龙坑")
# print(Hero.born_position)
print(Hero.get_born_position())
print(Hero._Hero__born_position)