class Weapon():
    def __init__(self, name:str, money:int, skill:dict, status:list, growth:list, level_delimiter:dict, wearing:str = None):
        self.name = name
        self.money = money
        self.wearing = wearing
        self.skill = skill
        self.status = status
        self.growth = growth
        self.level_delimiter = level_delimiter
        self.experiment = 0
        self.level = 0

    def equip(self, wearing_name:str):
        if not self.wearing == None:
            self.wearing = wearing_name
        else:
            self.wearing = None
        
    def add_experiment(self, get:int):
        learn_skill = []
        self.experiment = self.experiment + get
        while True:
            if self.level == 10:
                break
            if self.experiment >= self.level_delimiter[self.level + 1]:
                self.level = self.level + 1
                self.experiment = self.experiment - self.level_delimiter[self.level]
                for i in range(7):
                    self.status[i] = self.status[i] + self.growth[i]
                if not self.skill[self.level] == None:
                    learn_skill.append(self.skill[self.level])
            else:
                break
        return learn_skill
