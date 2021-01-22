import items
import magic

class NonPlayerCharacter():
	def __init__(self):
		raise NotImplementedError("do not create raw npc objects")

	def __str__(self):
		return self.name

class Trader(NonPlayerCharacter):
	def __init__(self):
		self.name = "trader"
		self.gold = "100"
		self.inventory = [items.CrustyBread(),items.CrustyBread(),items.CrustyBread(), items.HealingPotion(),items.HealingPotion(),items.ManaPotion(),items.ManaPotion()]

class WindMagicObelisk(NonPlayerCharacter):
	def __init__(self):
		self.name = "obelisk"
		self.spell_book = [magic.Wind_Bolt(), magic.Gust()]		