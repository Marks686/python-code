class Hero:
    hp = 1000
    def info(self,sex):
        print("我是一个{}英雄".format(sex))


anqila = Hero()
print(anqila.hp)
anqila.info("爆发的女法师")

yase = Hero()
yase.hp=3000
print(yase.hp)
yase.info("坦度很高的男")