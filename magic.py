import player
class Spell:
	def __init__(self):
		raise NotIMplementedError("Do not create raw spell objects!")

	def __str__(self):
		return self.name


class magic_missle(Spell):
	def __init__(self):
		self.name = "Magic Missile"
		self.discription = "A bolt of condensed magical power that you fling at an opponent."
		self.damage = 15
		self.mana = 10

class fire_ball(Spell):
	def __init__(self):
		self.name = "Fire Ball"
		self.discription = "A ball of fire that explodes on impact."
		self.damage = 20
		self.mana = 15

