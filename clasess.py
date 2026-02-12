import time
from random import randint

class Warrior:
    def __init__(self, hp, name, weapon, armor, money):
        self.hp = hp
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.money = money
    
    def deal_damage(self, enemy):
        r_dmg = randint(self.weapon.dmg_min, self.weapon.dmg_max)
        yron_brone = enemy.armor.defence - r_dmg
        if yron_brone >= 0:
            print(f"{self.name} не смог нанести урона {enemy.name}")
        elif yron_brone < 0:
            enemy.hp = enemy.hp + enemy.armor.defence - r_dmg
            print(f"{self.name} нанёс {r_dmg - enemy.armor.defence} урона {enemy.name}")
            print(f"у {enemy.name} осталось {enemy.hp}")



class Hero(Warrior):
    def __init__(self, hp, name, weapon, armor, money, magic):
        super().__init__(hp, name, weapon, armor, money)
        self.max_hp = hp
        self.magic = magic
        self.inventory = []

    def print_inventory(self):
        number = 0
        print(f"y tibia {self.money} deneg")
        print(f"y tibia {self.hp} hp")
        for item in self.inventory:
            number+=1
            print(f"{number}. {item.show_characteristics()}")

    def inventory_manager(self):
        while True:
            print(f"твоё оружие - {self.weapon.show_characteristics()}")
            print(f"твоя броня - {self.armor.show_characteristics()}")
            self.print_inventory()
            smena_ekipirovki = int(input("напиши число экипировки которую хочешь надеть или 0 чтобы выйти"))
            smena_ekipirovki = smena_ekipirovki - 1
            if smena_ekipirovki == -1:
                break
            elif smena_ekipirovki in list(range(len(self.inventory))):
                self.use_eqipment(smena_ekipirovki)

    def use_heal_potion(self):
        heal_potions = []
        number = 1
        for i in self.inventory:
            if isinstance(i, Potion):
                heal_potions.append(i)
                print(f"{number}. {i.name}")
                number = number + 1
        vibor_zelia = int(input("выбери зелье"))
        if vibor_zelia >  len(heal_potions) or vibor_zelia < 1:
            print("такого зелья нет")
        else:
            vibor_zelia = vibor_zelia - 1
            self.hp = self.hp + heal_potions[vibor_zelia].regeneration
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp = self.hp
                self.inventory.remove(heal_potions[vibor_zelia])
        print(f"у тебя осталось {self.hp} здоровья")

    def use_eqipment(self, n_ekipirovki):
        if isinstance(self.inventory[n_ekipirovki], Armor):
            arxiv = self.inventory.pop(n_ekipirovki)
            self.inventory.append(self.armor)
            self.armor = arxiv
        elif isinstance(self.inventory[n_ekipirovki], Weapon):
            arxiv_weapona = self.inventory.pop(n_ekipirovki)
            self.inventory.append(self.weapon)
            self.weapon = arxiv_weapona
        elif isinstance(self.inventory[n_ekipirovki], Potion):
            self.hp = self.hp + self.inventory[n_ekipirovki].regeneration
            self.inventory.pop(n_ekipirovki)
        elif isinstance(self.inventory[n_ekipirovki], Magic):
            stick_arxiv = self.inventory.pop(n_ekipirovki)
            self.inventory.append(self.magic)
            self.magic = stick_arxiv

    def magic_dmg(self, enemy):
        if self.magic == None:
            print("у тебя нет магии")
            return
        else:
            enemy.hp == enemy.hp - self.magic.dmg
            print(f"{self.name} нанёс {self.magic.dmg} урона {enemy.name}")
            print(f"у {enemy.name} осталось {enemy.hp}")

class Weapon:
    def __init__(self, name, dmg_min, dmg_max, price):
        self.name = name
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self.price = price

    def show_characteristics(self):
        return f"{self.name}, dmg: {self.dmg_min} - {self.dmg_max}, price: {self.price}"

class Armor:
    def __init__(self, name, defence, price):
        self.name = name
        self.defence = defence
        self.price = price

    def show_characteristics(self):
        return f"{self.name}, defence: {self.defence}, price: {self.price}"
    
class Magic:
    def __init__(self, name, dmg, price):
        self.name = name
        self.dmg = dmg
        self.price = price

    def show_characteristics(self):
        return f"{self.name}, dmg: {self.dmg}, price: {self.price}"
    

class Potion:
    def __init__(self, name, regeneration, price):
        self.name = name
        self.regeneration = regeneration
        self.price = price

    def show_characteristics(self):
        return f"{self.name}, regeneration: {self.regeneration}, price: {self.price}"

class Room:
    def __init__(self, enemy):
        self.enemy = enemy

    def enter(self, hero):
        print(f"Вы входите в комнату {self.enemy.name} с {self.enemy.weapon.name}")
        self.fight(self.enemy, hero)


    def fight(self, enemy, hero):
        while hero.hp > 0 and enemy.hp > 0:
            fight_vibor = int(input("выбери действие: 1 ударить оружием, 2 выпить зелье, 3 ударить магией"))
            if fight_vibor == 2:
                hero.use_heal_potion()
            elif fight_vibor == 1:
                hero.deal_damage(enemy)
            elif fight_vibor == 3:
                hero.magic_dmg(enemy)
            if enemy.hp > 0:
                enemy.deal_damage(hero)
        if hero.hp > 0:
            winner = hero
            hero.money = hero.money + enemy.money
            hero.inventory.append(enemy.weapon)
            hero.inventory.append(enemy.armor)
        else:
            winner = enemy
        print(f"победил {winner.name}")
        if winner == hero:
            print(f"Ты победил. Ты получил {enemy.money} денег, {enemy.weapon.name}, {enemy.armor. name}.")
        else:
            print("Тебя убили... Возвращайся позже")
            
        

class Dungeon:
    def __init__(self, rooms, hero):
        self.rooms = rooms
        self.index = 0
        self.hero = hero
     

    def next(self):
        room = self.rooms[self.index]
        room.enter(self.hero)
        self.index += 1
        time.sleep(1)

class Magazin:
    def __init__(self, money, tovari):
        self.money = money
        self.tovari = tovari

    def start_trade(self, hero: Hero):
        while True:
            torg_vibor = int(input("напиши 1 продать товар, 2 купить товар, 3 выйти: "))
            if torg_vibor == 1:
                hero.print_inventory()
                n_tovara = int(input("выбери товар который хочешь продать?"))
                self.sell_tovar(hero, n_tovara)
            elif torg_vibor == 2:
                self.show_tovar()
                n_tovara = int(input("выбери товар который хочешь купить"))
                self.buy_tovar(hero, n_tovara)
            elif torg_vibor == 3:
                break
            else:
                print("нет такой опции")

    def show_tovar(self):
        nomer = 0
        for item in self.tovari:
            nomer+=1
            print(f"{nomer}. {item.show_characteristics()}")

    def buy_tovar(self, hero: Hero, n_tovara: int):
        if n_tovara > len(self.tovari):
            print("Нет такого товара")
        else:
            n_tovara = n_tovara - 1
            if hero.money >= self.tovari[n_tovara].price:
                hero.money = hero.money - self.tovari[n_tovara].price
                self.money = self.money + self.tovari[n_tovara].price
                print(f"tovar {self.tovari[n_tovara].name} bil kyplen")
                hero.inventory.append(self.tovari[n_tovara])
                self.tovari.pop(n_tovara)
            else:
                print("y tibya nexvataet deneg")
            
    def sell_tovar(self, hero: Hero, n_tovara: int):
        if n_tovara > len(hero.inventory):
            print("net takovo tovara")
        else: 
            n_tovara = n_tovara - 1
            if self.money >= hero.inventory[n_tovara].price:
                self.money = self.money - hero.inventory[n_tovara].price
                hero.money = hero.money + hero.inventory[n_tovara].price
                print(f"tovar {hero.inventory[n_tovara].name} bil prodan")
                self.tovari.append(hero.inventory[n_tovara])
                hero.inventory.pop(n_tovara)
            else:
                print("y torgovza ne xvataet deneg")