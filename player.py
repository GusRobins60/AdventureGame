import items
import world
import enemies
import magic
import json

class Player:
	
	def __init__(self):
		self.inventory = [items.Dagger(),items.Rock(),items.CrustyBread(),items.ManaPotion()]
		self.spell_book = [magic.magic_missle(), magic.fire_ball()]
		self.x = world.start_tile_location[0]
		self.y = world.start_tile_location[1]
		self.hp = 100
		self.gold = 5
		self.victory = False
		self.exp = 199
		self.player_lvl = 1
		self.mp = 100
	def is_alive(self):

		return self.hp > 0 
	def move(self,dx,dy):
		self.x += dx
		self.y += dy
	def move_north(self):
		self.move(dx=0, dy=-1)
	def move_south(self):
		self.move(dx=0, dy=1)
	def move_east(self):
		self.move(dx=1, dy=0)
	def move_west(self):
		self.move(dx=-1, dy=0)
	def player_stats(self):
		print("Level: {}".format(self.player_lvl), "HP: {}".format(self.hp),"Mana:{}".format(self.mp),"Gold: {}".format(self.gold), "EXP: {}".format(self.exp))
	def print_spellbook(self):
		print('\n Spell Book')
		for magic in self.spell_book:
			print('*'+str(magic))

	def print_inventory(self):
		print("\n Inventory:")
		for item in self.inventory:
			print('* ' + str(item))
		print("Gold: {}".format(self.gold))
	

	'''
	def check_lvl_up(self,enemy):
		new_exp = self.exp + enemy.exp
		levels = [0,200,450,1012]
		if True:
			current_level = sum(1 for x in levels if x<= total_exp)
			self.player_lvl = current_level
	'''
	def learn_magic(self):
		pass
	def most_powerful_weapon(self):
		max_damage = 0 
		best_weapon = None
		for item in self.inventory: 
			try:
				if item.damage > max_damage:
					best_weapon = item 
					max_damage = item.damage
					if self.player_lvl >= 2:
						item.damage = item.damage + 1
						spell.damage += 1
					elif self.player_lvl >= 3:
						item.damage = item.damage + 2
						spell.damage += 2
			except AttributeError:
				pass

		return best_weapon
	def attack(self):

		spell = [magic_spell for magic_spell in self.spell_book if isinstance(magic_spell,magic.Spell)]
		if not spell:
			print("\nYou have no spells to cast!")
		
		user_input = input('\nWhat do you want to attack with? melee or magic: ')
	
		if user_input == 'magic':
			print("\nChoose a spell to cast: ")
			for i, magic_spell in enumerate(spell, 1):
				
				print("{}. {}".format(i,magic_spell))
			
			valid =False
			while not valid:
				choice = input("")
				try:
					if self.mana == 0:
						print("You dont have enough mana")
					else:	
						room = world.tile_at(self.x,self.y)
						enemy = room.enemy
						print("\nYou use {} against {}!".format(magic_spell,enemy.name))
						enemy.hp -= magic_spell.damage
						self.mp = self.mp - magic_spell.mana

						if not enemy.is_alive():
							print("\nYou killed {}!".format(enemy.name))
							
						else:
							print("{} HP is {}.".format(enemy.name,enemy.hp))
				except(ValueError,IndexError):
					print("Invalid choice, try again")	
				break
		elif user_input == 'melee':
			best_weapon = self.most_powerful_weapon()
			room = world.tile_at(self.x,self.y)
			enemy = room.enemy
			print("You use {} against {}!".format(best_weapon.name,enemy.name))
			enemy.hp -=  best_weapon.damage

			if not enemy.is_alive():
				print("You killed {}!".format(enemy.name))
				
			else:
				print("{} HP is {}.".format(enemy.name,enemy.hp))

	def heal(self):
		consumables = [item for item in self.inventory if isinstance(item,items.Consumables)]
		if not consumables:
			print("You dont have any items to heal you!")
			return 

		for i, item in enumerate(consumables, 1):
			print("Choose an item to use to heal: ")
			print("{}. {}".format(i, item))
		
		valid = False
		while not valid:
			choice = input("")
			try:
				to_eat = consumables[int(choice)-1]
				self.hp = min(100,self.hp + to_eat.healing_value)
				self.inventory.remove(to_eat)
				print("Current HP: {}".format(self.hp))
				valid = True
			except (ValueError,IndexError):
				print("Invalid choice, try again")
	def mana(self):
		restore_mana = [item for item in self.inventory if isinstance(item,items.ManaRestore)]
		if not restore_mana:
			print("You dont have anything to restore mana")
			return
		for i,item in enumerate(restore_mana,1):
			print("choose an item to restore mana.")
			print("{}. {}".format(i, item))

		valid = False
		while not valid:
			choice = input("")
			try:
				to_restore = restore_mana[int(choice)-1]
				self.mp = min(100,self.mp + to_restore.mana_value)
				self.inventory.remove(to_restore)
				print("Current MP: {}".format(self.mp))
				valid = True
			except (ValueError, IndexError):
				print("invalid choice, try again")
	def learn_magic(self):
		room = world.tile_at(self.x,self.y)
		room.check_if_learn_spell(self)
		
	def trade(self):
		room = world.tile_at(self.x,self.y)
		room.check_if_trade(self)
	
	def current_locaton(self):
		room = world.tile_at(self.x,self.y)
		self.current_location = room

	def saveload(self):
		player_Stats = {
			self.player.hp,
			self.player.gold,
			self.player.lvl,
			self.player.current_location(),
		}
		filename = 'save.json'
		with open(filename, 'w') as f:
			json.dump(player_Stats)
		
