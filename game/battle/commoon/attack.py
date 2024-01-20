class Attack():
    def __init__(self, turn_player, target):
        self.turn_player = turn_player
        self.target = target

    def do_attack(self):
        if self.turn_player.get_attack() > self.target.get_difence():
            damage = self.turn_player.get_attack() - self.target.get_difence()
        else:
            damage = 1
            
        self.target.set_hp(self.target.get_hp() - damage)

        if self.target.get_hp() <= 0:
            return True
        else:
            return False