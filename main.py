from character import *
from battle import *

star = "\U0001F320"
dragon = "\U0001F432"
rainbow = "\U0001F308"
stop = "\U0001F6AB"
fairy = "\U0001F9DA"



print("==============="+rainbow+"GAME START"+rainbow+"===============")

print("게임 설명 : 스파르타 왕국에 침입한 몬스터를 물리쳐라!\n\n   1. 플레이어는 일반공격와 마법공격을 통해 몬스터를 물리치고, 포인트를 얻을 수 있습니다.\n   2. 마법공격은 한 번 공격시 mp 100을 소모하고, mp 500으로 게임을 시작합니다. \n   3. 각 라운드가 끝나면 포인트를 이용해 상점에서 아이템을 살 수 있습니다.\n   4. 최종 라운드까지 무사히 도착해서 BOSS를 물리치고 평화를 되찾아주세요!\n\n\n")

player_name = input('Enter name: ')

my_player = player(player_name, 1000, 25)
my_monster = Monster()
round = 0


while round < 3:
    round += 1
    my_monster.set_monster_level(round)

    store(my_player)

    print("\n"+"="*15 + f"ROUND {round}" + "="*15)

    battle(my_player,my_monster)

    if my_player.hp == 0:
        print(f"Round{round} : 패배하였습니다. 다시 도전해주세요")
        break
    else:
        new_point = 100*round+50
        print(f"Round{round} : 승리하였습니다!\n {new_point} 포인트 획득!")
        my_player.point += new_point


if my_player.hp != 0:
    print(rainbow+"스파르타 성을 무사히 구했습니다! 당신을 최고의 용사로 임명합니다"+rainbow)
