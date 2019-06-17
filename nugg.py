import random
import os
import time
import sys

class Player:
    def __init__(self, username):
        self.username = username
        self.name = 'John'
        self.health = 100
        self.level = 1
        self.location = 'Cave'
        self.coordinates = [0, 0]
        self.inventory = ['Phone']
        self.objective = 'Find a way out'
        self.attack = 5
        self.gold = 0
        self.exp = 0
        self.kill_count = 0

    def show_stats(self):
        print("")
        print('Name: '+self.name)
        print('Health: '+str(self.health))
        print('Level: '+str(self.level))
        print('Gold: '+str(self.gold))
        print('Location: '+self.location)
        # print('Coordinates: '+str(self.coordinates))
        print("")

    def add_inventory(self, item):
        self.inventory.append(item)

    def rem_inventory(self):
        print("which item would you like to remove?")
        item = int(input(">Your Choice: "))
        item -= 1
        if item != 0:
            print(self.inventory[item] + " has been removed!")
            self.inventory.pop(item)
        else:
            print(self.inventory[item] + " cannot be removed")

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("Your backpack is empty")
            print("")
        else:
            place = 1
            print("")
            print("Your items:")
            for item in self.inventory:
                print(str(place) + ' - ' + item)
                place += 1

    def use_inventory(self):
        running = True
        while (running):
            self.show_inventory()
            print("")
            print("Available actions:")
            print("1 - Use phone to shop")
            print("2 - Use item")
            print("3 - Drop item")
            print("0 - Leave inventory")
            choice = int(input(">Your Choice: "))
            if choice == 1:
                Shop(self)
            elif choice == 2:
                self.use_item()
            elif choice == 3:
                self.rem_inventory()
            else:
                running = False

    def use_item(self):
        print("Which item would you like to use?")
        choice = int(input(">Your choice: "))
        choice -= 1
        if self.inventory[choice] == 'health potion':
            self.health += 10
            if self.health > 100:
                self.health = 100
            print("")
            print("You used a health potion! Health increased by 10")
            self.inventory.pop(self.inventory.index('health potion'))
        elif self.inventory[choice] == 'Phone':
            Shop(self)
        else:
            print("")
            print("You can't use this item")


    def add_gold(self, ammount):
        self.gold += ammount

    def save_info(self):
        print("Would you like to save your score?[y, n]")
        choice = input(">Your choice: ")
        if choice == 'y':
            f = open('Scores.txt', 'a')
            f.write(self.username + ":" + " level: " + str(self.level) + " creatures killed: " + str(self.kill_count) \
                    + " experience: " + str(self.exp) + "\n")
            f.close()
        else:
            pass

    def get_exp(self, enemy):
        if enemy.level < 5:
            experience = random.randint(5, 10)
        elif enemy.level >= 5 and enemy.level < 10:
            experience = random.randint(10, 30)
        elif enemy.level >= 10 and enemy.level < 50:
            experience = random.randint(30, 50)

        self.exp += experience
        print("You got " + str(experience) + " XP!")
        self.level_up()

    def level_up(self):
        if self.exp >= 5 and self.exp < 10:
            self.level += 1
            print("")
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 10 and self.exp < 20:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 20 and self.exp < 30:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 30 and self.exp < 40:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 40 and self.exp < 60:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 60 and self.exp < 100:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 100 and self.exp < 140:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 140 and self.exp < 180:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 180 and self.exp < 250:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")
        elif self.exp >= 250 and self.exp < 400:
            self.level += 1
            print("You've reached level " + str(self.level) + "!")

class Enemy:
    def __init__(self):
        self.name = 'Rock'
        self.level = '1'
        self.health = '10000'
        self.attack = '0'

    def generate(self, player):
        creature_name = [
            'Evil Spider',
            'Evil Slug',
            'Night Walker',
            'Haunted Lantern'
        ]
        self.name = random.choice(creature_name)
        if player.level < 3:
            self.level = random.randint(1, 5)
            self.health = random.randint(10, 40)
            self.attack = random.randint(2, 5)
        elif player.level >= 3 and player.level < 10:
            self.level = random.randint(5, 10)
            self.health = random.randint(40, 100)
            self.attack = random.randint(5, 10)
        elif player.level >= 10 and player.level < 50:
            self.level = random.randint(10, 50)
            self.health = random.randint(80, 200)
            self.attack = random.randint(10, 20)

    def drop_loot(self, player):
        item = loot(self.level)
        print(self.name + " dropped a " + item + '!')
        print("Take it?[y,n]")
        choice = input(">Your Choice:")
        choosing = True
        while (choosing):
            if choice == 'y':
                player.add_inventory(item)
                print("")
                print(item + " has been added to your inventory!")
                choosing = False
            elif choice == 'n':
                choosing = False


    def drop_gold(self, player):
        ammount = 0
        if self.level < 10:
            ammount = random.randint(5, 11)
        elif self.level >= 10 and self.level < 15:
            ammount = random.randint(10, 30)
        elif self.level >= 15 and self.level < 40:
            ammount = random.randint(10, 30)
        else:
            ammount = 1

        print(self.name + " dropped " + str(ammount) + " gold")
        player.add_gold(ammount)

class Shop_dude:
    def __init__(self):
        self.name = 'Shop dude'
        self.items = [
            'sword',
            'armor',
            'shield',
            'health potion'
        ]
        self.thingies = {
            'sword': 100,
            'armor': 50,
            'shield': 200,
            'health potion': 5
        }

    def initiate_dialogue(self, player):
        print("")
        print(self.name + ": " + "Hi, Jon")
        print("Your gold: " + str(player.gold))
        print("")

    def show_items(self, player):
        i = 1
        #shows items to be sold
        for key, cost in self.thingies.items():
            print(str(i)+' - '+str(key), str(cost)+' gold')
            i += 1
        print("Found anything you like?[1-" + str(len(self.items)) + "/ 0 to exit]")
        choice = int(input(">Your choice: "))
        if choice >= 0 and choice <= len(self.items):
            self.sell_item(player, choice)
        elif choice == 0:
            return False

    def sell_item(self, player, choice):
        #every option is 1 less cause list starts from 0 owo
        choice -= 1
        if choice == 3:
            if player.gold >= self.thingies['health potion']:
                item = self.items[choice]
                player.inventory.append(item)
                print("You bought a health potion!")
            else:
                print("Not enough money!")
        elif choice == 0:
            if player.gold >= self.thingies['sword']:
                item = self.items[choice]
                player.inventory.append(item)
                print("You bought a sword!")
            else:
                print("Not enough money!")
        elif choice == 1:
            if player.gold >= self.thingies['armor']:
                item = self.items[choice]
                player.inventory.append(item)
                print("You bought armor!")
            else:
                print("Not enough money!")
        elif choice == 2:
            if player.gold >= self.thingies['shield']:
                item = self.items[choice]
                player.inventory.append(item)
                print("You bought a shield!")
            else:
                print("Not enough money!")

#random loot
def loot(level):


    loot = [
    #common_loot
        'health potion',
        'stick',
    #uncommon_loot
        'magic sphere',
        'legendary chicken nugget',
        'pet bat',
        'magical paper'
    ]

    if level >= 1 and level <= 10:
        x = random.randint(1, 10)
        if x <= 2:
            #health potion
            return loot[0]
        else:
            #a stick
            return loot[1]

    if level > 10 and level <= 100:
        x = random.randint(1, 20)
        if x < 5:
            #magic sphere
            return loot[2]
        elif x >= 5 and x <= 10:
            #legendary chicken nugget
            return loot[3]
        elif x > 10 and x <=18:
            #a pet bat
            return loot[4]
        else:
            #magical paper
            return loot[5]

#action menu
def action_menu():
    print("------------------------------------")
    print("1 - Move North")
    print("2 - Move East")
    print("3 - Move South")
    print("4 - Move West")
    print("")
    print("5 - Check Inventory")
    print("6 - Check Stats")
    print("7 - Check objective")
    print("")
    print("0 - quit")
    print("------------------------------------")

def Shop(player):
    cashier = Shop_dude()
    shopping = True
    while (shopping):
        cashier.initiate_dialogue(player)
        shopping = cashier.show_items(player)

#choose an action
def action(player):
    running = True
    while running:
        action_menu()
        choosing = True
        choice = int(input(">Choose an action: "))

        if choice == 5:
            player.use_inventory()
        elif choice == 6:
            player.show_stats()
        elif choice == 7:
            print("")
            print('Current objective: ' + player.objective)
            print("")
        elif choice > 0 and choice < 5:
            move(choice, player)
            #engage fight
            fight_random(player)
        elif choice == 0:
            player.save_info()
            sys.exit()

#movement
def move(choice, player):
    if choice == 1:
        print("you went North")
        print("")
        player.coordinates[0] += 1
    elif choice == 2:
        print("you went East")
        print("")
        player.coordinates[1] += 1
    elif choice == 3:
        print("you went South")
        print("")
        player.coordinates[0] -= 1
    elif choice == 4:
        print("you went West")
        print("")
        player.coordinates[1] -= 1

#Checks if player walked in on a creature
def fight_random(player):
    fight = random.randint(1, 100)
    if fight < 50:
        enemy = Enemy()
        enemy.generate(player)
        print("You've been booped by " + enemy.name + "!")
        print("")
        print("Engage in a fight?[y, n]")
        choice = input(">Your choice: ")
        if choice == 'y':
            engage_fight(player, enemy)
        else:
            print("The creature wobbled away.")
    else:
        return

#the actual battle
def engage_fight(player, enemy):
    print("")
    print("---battle mode---")
    running = True

    while(running):
        print("")
        print("-----------------")
        print("Your health: " + str(player.health))
        print(enemy.name + "'s health: " + str(enemy.health))
        print("-----------------")

        #Player does a do
        print("Your move: ")
        print("1 - attack")
        print("2 - throw an item")
        print("0 - Flee")
        if 'health potion' in player.inventory:
            print("3 - Use health potion")
        c = int(input(">Your choice: "))
        if c == 1:
            enemy.health -= player.attack
        elif c == 2:
            throw_item(player, enemy)
        elif c == 3:
            player.health += 10
            print("")
            print("You used a health potion! Health increased by 10")
            player.inventory.pop(player.inventory.index('health potion'))
        elif c == 0:
            print("")
            print("You fled the fight")
            print(enemy.name + " wobbled away")
            running = False

        #Enemy does a do
        print("")
        print(enemy.name + " slapped you!")
        player.health -= enemy.attack


        #someone looses
        if enemy.health <= 0:
            print("")
            print("You killed " + enemy.name)
            print("")
            enemy.drop_gold(player)
            enemy.drop_loot(player)
            player.get_exp(enemy)
            player.kill_count += 1
            running = False
        if player.health <= 0:
            print("")
            print(enemy.name + " knocked you out!")
            player.health += 1
            running = False
    return 0

#If player throws an item at the enemy. Used in 'engage fight' function
def throw_item(player, enemy):
    player.show_inventory()
    print("Which item would you like to throw at " + enemy.name + "?")
    thrown_item = int(input(">Your choice: "))
    thrown_item -= 1
    if player.inventory[thrown_item] == 'Phone':
        print("")
        print("You threw a phone!")
        if player.gold >= 5:
            print(enemy.name + " used it to buy themselves a health potion")
            print("You lost 5 gold")
            enemy.health += 10
            player.gold -= 5
            print("You picked up your phone")
        else:
            print("You missed")
    elif player.inventory[thrown_item] == 'health potion':
        print("")
        print("Oh?")
        print(enemy.name + " caught and drank the health potion!")
        print(enemy.name + "'s health increased by 10")
        player.inventory.pop(player.inventory.index('health potion'))
    else:
        miss = random.randint(1, 50)
        damage = random.randint(1, 20)
        if miss < 40:
            print(player.inventory[thrown_item] + " did " + str(damage) + " damage to " + enemy.name)
        else:
            print("You missed. " + player.inventory[thrown_item] + " fell through a crack in the floor. It's gone")

def score_file():
    try:
        with open("Scores.txt", "r") as f:
            for line in f:
                print(line)
            f.close()
    except IOError:
        print("There is no scores file")

def start():
    running = True

    while (running):
        count = 1
        print("=========================")
        print("\t" + str(count) + " - START")
        count +=1
        print("\t" + str(count) + " - SCORES")
        print("\t" + "0 - QUIT")
        print("=========================")
        c = int(input(">Your Choice: "))
        if c == 1:
            print("Enter your username: ")
            username = input(">")
            player = Player(username)
            chapter1(player)
        elif c == 0:
            print("game over")
            running = False
        elif c == 2:
            score_file()
def chapter1(player):

    print("")
    print("You're Jon. You're in a cave. Find a way out.")
    print("")

    action(player)

start()