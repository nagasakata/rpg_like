class PlayerInfo():
    def __init__(self):
        self.member_all = []
        self.money  = 0
        self.item_dict = {'consumption':{}, 'weapon':{}, 'material':{}, 'other':{}}

    def add_money(self, money:int):
        self.money = self.money + money