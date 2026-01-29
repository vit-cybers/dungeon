from clasess import Warrior, Hero, Weapon, Room, Dungeon, Armor, Magazin, Potion
import random


bow = Weapon("bow", 20, 28, 230)
sword = Weapon("sword", 31, 35, 320)
hands = Weapon("hand", 8, 12, 0)
claws = Weapon("claws", 15, 19, 164)
sekira = Weapon("sekira", 26, 29, 290)
kinjal = Weapon("kinjal", 10, 16, 130)
knife = Weapon("knife", 14, 18, 140)
bylava = Weapon("bylava", 30, 45, 320)
golem_fists = Weapon("golem fists", 16, 21, 154)
wizzard_staff = Weapon("wizzard staff", 23, 30, 270)
witch_staff = Weapon("witch staff", 22, 30, 333)
dragon_claw = Weapon("dragon claw", 57, 70, 1730)
legendary_sword = Weapon("legendary sword", 56, 64, 2899)
super_bow = Weapon("super bow", 46, 54, 1450)

iron_armor = Armor("iron armor", 14, 267)
leather_armor = Armor("leather armor", 13, 193)
hide = Armor("hide", 6, 87)
cloak = Armor("cloak", 9, 143)
stone_armor = Armor("stone armor", 16, 303)
dragon_armor = Armor("dragon armor", 23, 1170)

swordman = Warrior(84, "swordman", sword, iron_armor, 77)
bowman = Warrior(68, "bowman", bow, leather_armor, 64)
rat = Warrior(53, "rat", claws, hide, 41) 
goblin = Warrior(40, "goblin", kinjal, iron_armor, 31)
skeleton = Warrior(64, "skeleton", knife, leather_armor, 36)
wizzard = Warrior(72, "wizzard", wizzard_staff, cloak, 67)
goblin_king = Warrior(120, "goblin king", bylava, hide, 120)
golem = Warrior(163, "golem", golem_fists, stone_armor, 134)
witch = Warrior(105, "witch", witch_staff, cloak, 96)
dragon = Warrior(174, "dragon", dragon_claw, dragon_armor, 201)

hero = Hero(109, "hero", sword, iron_armor, 1000)

sm_reg_potion = Potion("small regeneration potion", 29, 71)
med_reg_potion = Potion("meidium regeneration potion", 57, 204)
big_reg_potion = Potion("big regeneration potion", 99, 530)

torgovez = Magazin(9000, [super_bow, legendary_sword, dragon_armor, sm_reg_potion, med_reg_potion, big_reg_potion])

room1 = Room(skeleton)
room2 = Room(goblin)
room3 = Room(rat)
room4 = Room(bowman)
room5 = Room(wizzard)
room6 = Room(swordman)
room7 = Room(goblin_king)
room8 = Room(golem)
room9 = Room(witch)
room10 = Room(dragon)

weak_rooms = [room1, room2, room3]
medium_rooms = [room4, room5, room6]
hard_rooms = [room7, room8, room9]
boss_room = [room10]

rooms = []

random.shuffle(weak_rooms)
random.shuffle(medium_rooms)
random.shuffle(hard_rooms)
rooms.extend(weak_rooms)
rooms.extend(medium_rooms)
rooms.extend(hard_rooms)
rooms.extend(boss_room)

dung1 = Dungeon(rooms, hero)
while True:
    if hero.hp <= 0:
        break
    else:
        print("выберите действие")
        print("1. открыть новую дверь 2. магазин 3. инвентарь")
        vibor = int(input())

        if vibor == 1:
            dung1.next()
        elif vibor == 2:
            torgovez.start_trade(hero)
        elif vibor == 3:
            hero.inventory_manager()
        else:
            print("что-то не то. Напиши ещё раз.")