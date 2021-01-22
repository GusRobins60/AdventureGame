<<<<<<< HEAD
import player
class Spell:
	def __init__(self):
		raise NotIMplementedError("Do not create raw spell objects!")

	def __str__(self):
		return self.name


class magic_missle(Spell):
	def __init__(self):
		self.name = "Magic Missle"
		self.discription = "A bolt of condensed magical power that you fling at an opponent."
		self.damage = 15
		self.mana = 10

class fire_ball(Spell):
	def __init__(self):
		self.name = "Fire Ball"
		self.discription = "A ball of fire that explodes on impact."
		self.damage = 20
		self.mana = 15

class Wind_Bolt(Spell):
	def __init__(self):
		self.name = 'Wind Bolt'
		self.disription = "A compressed bolt of air directed at you enemy."
		self.damage = 25
		self.mana = 20 

class Gust(Spell):
	def __init__(self):
		self.name = 'Gust'
		self.discription = "Heavy gust of wind that damages enemeies"
		self.damage = 5
		self.mana = 5


=======
import player
class Spell:
	def __init__(self):
		raise NotIMplementedError("Do not create raw spell objects!")

	def __str__(self):
		return self.name


class magic_missle(Spell):
	def __init__(self):
		self.name = "Magic Missle"
		self.discription = "A bolt of condensed magical power that you fling at an opponent."
		self.damage = 15
		self.mana = 10

class fire_ball(Spell):
	def __init__(self):
		self.name = "Fire Ball"
		self.discription = "A ball of fire that explodes on impact."
		self.damage = 20
		self.mana = 15

class Wind_Bolt(Spell):
	def __init__(self):
		self.name = 'Wind Bolt'
		self.disription = "A compressed bolt of air directed at you enemy."
		self.damage = 25
		self.mana = 20 

class Gust(Spell):
	def __init__(self):
		self.name = 'Gust'
		self.discription = "Heavy gust of wind that damages enemeies"
		self.damage = 5
		self.mana = 5


>>>>>>> 45bf0b496c1d4f59d90e5c29989043ba435b2ac7
