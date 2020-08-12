import player

class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw weapon objects.")
		
	def __str__(self):
		return self.name


class Consumables:
	def __init__(self):
		raise NotImplementedError("Do not create raw consumable objects")

	def __str__(self):
		return "{} (+{} HP)".format(self.name, self.healing_value)

class CrustyBread(Consumables):
	def __init__(self):
		self.name = "Crusty Bread"
		self.healing_value = 10
		self.value = 12

class Rock(Weapon):
	def __init__(self):
		self.name = "Rock"
		self.discription = "A fist sized rock, suitable for bludgeoning."
		self.damage = 5
		self.value = 1

class Dagger(Weapon):
	def __init__(self):
		self.name = "Dagger"
		self.discription = "a small dagger with some rust."\
							"Somewhat more dangerous than a Rock."
		self.damage = 10 
		self.value = 20

class RustySword(Weapon):
	def __init__(self):
		self.name = "Rusty Sword"
		self.discription = "This sword is showing its age,"\
							"but still has some fight in it."
		self.damage = 20
		self.value = 100

class HealingPotion(Consumables):
	def __init__(self):
		self.name = "Healing Potion"
		self.healing_value = 50
		self.value = 60
