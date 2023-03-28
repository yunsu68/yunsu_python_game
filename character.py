import random

star = "\U0001F320"
dragon = "\U0001F432"
rainbow = "\U0001F308"
stop = "\U0001F6AB"
fairy = "\U0001F9DA"
sword = "\U0001F5E1"


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 5, self.power + 10)
        other.hp = max(other.hp - damage, 0)
        print(f"\n{sword}{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."+sword+"\n")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class player(Character):
    '''
        플레이어
    '''
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.point = 0
        self.max_mp = 500
        self.mp = 500

    def magic_attack(self, other):
        magic_damage = random.randint(100, 155)
        self.mp -= 100
        other.hp = max(other.hp - magic_damage, 0)
        print("\n"+fairy+f"{self.name}의 마법공격! {other.name}에게 {magic_damage}의 데미지를 입혔습니다."+fairy+"\n")
        print(f"플레이어의 mp가 100감소 하였습니다. (mp : {self.mp}/{self.max_mp})")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        return super().show_status()


class Monster(Character):
    '''
     몬스터
    '''
    def __init__(self):
        self.name = "monster"
        self.max_hp = 250
        self.hp = 250

        self.power = 20

    def set_monster_level(self, level):
        self.level = level
        if level == 1:
            self.max_hp = 250
            self.hp = 250
        if level == 2:
            self.max_hp = 450
            self.hp = 450
        if level == 3:
            self.max_hp = 650
            self.hp = 650

    def attack(self, other):
        if self.level == 1:
            damage = random.randint(20 - 5, 20 + 5)
            other.hp = max(other.hp - damage, 0)
            print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")
        if self.level == 2:
            attack_type = random.randint(1, 10)
            if attack_type > 5:
                print(dragon+"몬스터가 불 공격을 합니다"+dragon)
                damage = random.randint(60, 90)
            else:
                damage = random.randint(30, 60)
            other.hp = max(other.hp - damage, 0)
            print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")
        if self.level == 3:
            attack_type = random.randint(1, 10)
            if attack_type > 8:
                print(star+"몬스터가 python 공격을 합니다"+star)
                damage = random.randint(145, 160)
            else:
                damage = random.randint(100, 125)
            other.hp = max(other.hp - damage, 0)
            print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")
