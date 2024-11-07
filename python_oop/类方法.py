class Hero:

    born_position = "泉水"
    def __init__(self,name,sex,hp,attack):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.attack = attack
    def info(self):
        print("我是一个英雄")

    @classmethod
    def where_was_i_born(cls):
        print("我在{}出生".format(cls.born_position))


Hero.where_was_i_born()