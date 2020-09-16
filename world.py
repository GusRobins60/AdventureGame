import enemies
import npc
import random
import time
import items





class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
      
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player): 
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        \n You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
        time.sleep(0.5)


class EnemyTile(MapTile):
    '''            
    def __init__(self, x, y):
    
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text =  "\nA giant spider jumps down from " \
                              "its web in front of you!"
                              
            self.dead_text = "\nThe corpse of a dead spider " \
                             "rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "\n An ogre is blocking your path!"
            self.dead_text = "\nA dead ogre reminds you of your triumph."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "\nYou hear a squeaking noise growing louder" \
                              "...suddenly you are lost in swarm of bats!"
            self.dead_text = "\nDozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "\nYou've disturbed a rock monster " \
                              "from his slumber!"
            self.dead_text = "\nDefeated, the monster has reverted " \
                             "into an ordinary rock."
        
        super().__init__(x, y)
    '''
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        time.sleep(0.1)
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))
        if not self.enemy.is_alive():
            player.gold = player.gold + self.enemy.gold
            if self.enemy.gold == 0:
                pass
            player.exp = player.exp + self.enemy.exp
            total_exp = player.exp
            levels = [0,200,450,1012]
            if True:
                current_level = sum(1 for x in levels if x <= total_exp)
                player.player_lvl = current_level
        
                if not self.enemy.is_alive():
                    self.enemy.exp = 0

class GoblinScoutTile(EnemyTile):
    def __init__(self,x,y):
        self.enemy = enemies.GoblinScout()
        r = random.random()
        if r < .20:
            self.alive_text = "\nA small goblin jumps out at you its not much to look at..."\
                                "Lookout its got a knife!"
        elif r < 50:
            self.alive_text = "\nOut of a dark recess in the wall jumps a goblin"\
                                " ready to scewer you with his dagger"
        else:
            self.alive_text = "\nYou hear a gutteral voice out of the dark "\
                                "walks a goblin ready for battle!"
        self.dead_text = "\nA dead goblin body."

        super().__init__(x, y)

class GoblinBasherTile(EnemyTile):
    def __init__(self,x,y):
        self.enemy = enemies.GoblinBasher()
        self.alive_text = "\nLookout a Goblin basher and he is looking for a fight."

        self.dead_text = "\n The body of a dead Goblin basher"
        super().__init__(x,y)


class VictoryTile(MapTile):
    def modify_player(self,player):
    	player.victory = True
    
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        Victory is yours!
        """


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Another unremarkable part of the cave. You must forge onwards.
            """
        else:
            return """
            Someone dropped some gold. You pick it up.
            """
          
class TrapRoomTile(MapTile):
    def __init__(self, x, y):
        r = random.randint(1,2)
        if r == 1:
            self.trap = items.PitFall()

            self.tripped_text = "The open hole of a Pit Fall trap obstructs the tunnel."

            self.set_text = "The floor in this hallway is unusually clean."

        else:
            return"""
            Looks like more bare stone...
            """
        super().__init__(x, y)
    
    def modify_player(self,player):
        if not self.trap.is_tripped():
            player.hp = player.hp - self.items.damage
            print("You stumbled into a trap!")
            time.sleep(1)
            print("\nTrap does {} damage. You have {} HP remaining.".
                  format(self.items.damage, player.hp))
    
    def intro_text(self):
        text = self.tripped_text if self.items.is_tripped() else self.set_text
        time.sleep(0.1)
        return text

class EmptyRoomTile(MapTile):
    def intro_text(self):
        r = random.random()
        if r < .10:
            return"""
            Rough hewn stone walls are all you can make out in the flickering tourch light.
            """
        elif r < .30:
            return"""
            There is nothing remarkable in this part of the tunnel keep moving onward!
            """
        elif r < .50:
            return"""
            The dirt in this part of th ecave is scuffed but otherise there is nothing
            remarkable here. best push on.
            """
        elif r < 70:
            return"""
            You've been walking for a while without finding anyone or anything.
            no sense in going back now better keep moving.
            """
        else:
            return"""
            Great more stone... Is that a breeze I feel better keep going.
            """



class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = int(seller.gold) + int(item.value)
        buyer.gold = int(buyer.gold) - int(item.value)
        print("Trade complete!")


    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in the corner
        clinking his gold coins together. He looks willing to trade.
        """

world_dsl = """
|EN|EN|VT|EN|EN|
|EN|  |  |  |EN|
|EN|FG|GS|  |TT|
|TT|  |ST|FG|EN|
|FG|  |TR|  |FG|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "GS": GoblinScoutTile,
                  "GB": GoblinBasherTile,
                  "ER": EmptyRoomTile,
                  "TR":TrapRoomTile,
                  "  ": None}


world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

