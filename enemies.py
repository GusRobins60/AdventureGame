import random

class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw empty enemy objects")
		
	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0
	


class GiantSpider(Enemy):
	def __init__(self):
		self.name = " Giant Spinder"
		self.hp = 10 
		self.damage = 2
		self.gold = 4
		self.exp = random.randint(10,30)

class Ogre(Enemy):
	def __init__(self):
		self.name = " Ogre"
		self.hp = 30
		self.damage = 10
		self.gold  = 20
		self.exp = random.randint(10,30)

class BatColony(Enemy):
	def __init__(self):
		self.name = "Colony of Bats"
		self.hp = 100
		self.damage = 4
		self.gold = 10
		self.exp = random.randint(10,30)

class RockMonster(Enemy):
	def __init__(self):
		self.name = "Rock Monster"
		self.hp = 80
		self.damage = 15
		self.gold = 50
		self.exp = random.randint(10,30) 

class GoblinScout(Enemy):
	def __init__(self):
		self.name = "Goblin Scout"
		self.hp = 20
		self.damage = random.randint(1,5)
		self.gold = 10
		self.exp = random.randint(5,10)

class GoblinBasher(Enemy):
	def __init__(self):
		self.name = "Goblin Basher"
		self.hp = 50
		self.damage = random.randint(5,10)
		self.gold = 15
		self.exp = random.randint(10,20)

