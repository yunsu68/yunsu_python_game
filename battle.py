
star = "\U0001F320"
dragon = "\U0001F432"
rainbow = "\U0001F308"
stop = "\U0001F6AB"
fairy = "\U0001F9DA"
gift = "\U0001F381"
money = "\U0001F4B0"


def store_items(my_player, item, count):
    if my_player.point < 100*count:
        print("\n"+stop+"포인트가 부족합니다!"+stop)
    else:
        if item == 1:                   #회복물약
            my_player.hp += 200*count
            my_player.point -= 100*count
        if item == 2:                   #강화물약
            my_player.power += 30*count
            my_player.point -= 100*count
        if item == 3:                   #마법물약
            my_player.mp += 100*count
            my_player.point -= 100*count


def store(my_player):
    print("\n"+"*"*15 + gift +"상점" + gift + "*"*15)
    item = 0
    while item != 4:
        print(
            f"\n내 포인트{money} : {my_player.point}\n1. 회복물약 (100p) : HP +200\n2. 강화물약 (100p) : 공격력 +30\n3. 마법물약 (100p) : mp +100 \n4. 상점 나가기\n")
        item = int(input("구매 할 상품 번호:"))
        if item != 4:
            count = int(input("상품 수량:"))
            store_items(my_player, item, count)
        
def battle(my_player,my_monster):
    while 1:

        my_player.show_status()
        my_monster.show_status()

        attack_type = 0

        attack_type = int(input(
            f'\n1) normal attack\n2) magic attack \n 공격 :'))

        if attack_type == 1:
            my_player.attack(my_monster)
            if my_monster.hp == 0:
                break
        elif attack_type == 2:
            if my_player.mp < 100:
                print("!!!마법 공격을 모두 이용했습니다!!!")
            else:
                my_player.magic_attack(my_monster)
                if my_monster.hp == 0:
                    break

        my_monster.attack(my_player)
        if my_player.hp == 0:
            break

    