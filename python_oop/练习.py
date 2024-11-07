class Hero:

    born_position = "泉水"
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


# Hero.where_was_i_born(
anqila = Hero("anqila","女",1000,500)
anqila.info()


class Game:
    top_score = 1029
    show_top_score = 231
    slow_help = "llllll"
    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def slow_help():
        slow_help = "llllll"