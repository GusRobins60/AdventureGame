import items
import world
import enemies
import magic

class Player:
	
	def __init__(self):
		self.inventory = [items.Dagger(),items.Rock(),items.CrustyBread()]
		self.spell_book = [magic.magic_missle(), magic.fire_ball()]
		self.x = world.start_tile_location[0]
		self.y = world.start_tile_location[1]
		self.hp = 100
		self.gold = 5
		self.victory = False
		self.exp = 199
		self.player_lvl = 1
		self.mana = 100
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
		print("Level: {}".format(self.player_lvl), "HP: {}".format(self.hp),"Gold: {}".format(self.gold), "EXP: {}".format(self.exp))
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
					self.stat_modifier()
			except AttributeError:
				pass

		return best_weapon
	def attack(self):
		spell = [magic for magic in self.spell_book if isinstance(magic,magic.Spell)]
		if not spells:
			print("You have no spells to cast!")
		
		input('What do you want to attack with? Melee or Magic: ')

		if input == 'magic':
			for i, magic in enumerate(spell, 1):
				print('Choose a spell to cast:')
				print(f"{i}. {spell}")
			valid =False
			while not valid:
				choice = input("")
				try:
					room = world.tile_at(self.x,self.y)
					enemy = room.enemy
					print("You use {} against {}!".format(spell,enemy.name))
					enemy.hp -=  spell.damage
					self.mana = self.mana - spell.mana

					if not enemy.is_alive():
						print("You killed {}!".format(enemy.name))
						
					else:
						print("{} HP is {}.".format(enemy.name,enemy.hp))
				except(ValueError,IndexError):
					print("Invalid choice, try again")

		elif input == 'melee':
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

	def trade(self):
		room = world.tile_at(self.x,self.y)
		room.check_if_trade(self)
	
	



	


