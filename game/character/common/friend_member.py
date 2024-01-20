from game.character.common.friend import Friend

class Member():
    def __init__(self):
        self.member = dict()

    def add_member(self, friend:Friend):
        if not (0 in self.member):
            self.member[0] = friend
        else:
            for i in self.member:
                if not (i+1) in self.member:
                    self.member[i+1] = friend
                    break
                if i == 2:
                    print("max member number is 4")
                    break

    def clear_member(self):
        self.member = {}

    def set_member(self, changed:Friend, new_friend:Friend):
        for i in self.member:
            if changed == self.member[i]:
                self.member[i] = new_friend
            if i == 3:
                print("something is wrong")

    def is_dead(self, die_character:Friend):
        for i in self.member:
            if die_character == self.member[i]:
                del self.member[i]

    def is_gameover(self):
        if self.member == {}:
            print("no member")
            return True
        else:
            return False

    def win_experiment(self, win:int):
        growth_dict = {}
        for i in self.member:
            growth_dict[self.member[i].get_name()] = self.member[i].add_experiment(win)

        return growth_dict


