level = 1

def check_level_up(self,player):
	player.exp = 400
	exp_lvl_cap = player.exp
		if new_exp == exp_lvl_cap:
			self.player_level = self.player_level + 1
			exp_lvl_cap = exp_lvl_cap + (int(exp_lvl_cap)*1.5)

