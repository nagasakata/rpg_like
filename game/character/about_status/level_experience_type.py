class LevelExperienceType():
    def __init__(self):
        self.l_e_list = []

    def early(self):
        self.l_e_list = []
        for i in range(99):
            self.l_e_list.append(int((10 + (10 * i/10)) * (i + 1)))
        return self.l_e_list

    def middle(self):
        self.l_e_list = []
        for i in range(99):
            self.l_e_list.append(int((15 + (10 * i/10)) * (i + 1)))
        return self.l_e_list

    def late_20(self):
        self.l_e_list = []
        for i in range(99):
            self.l_e_list.append(int((20 + (10 * i/10)) * (i + 1)))
        return self.l_e_list

    def late_30(self):
        self.l_e_list = []
        for i in range(99):
            self.l_e_list.append(int((30 + (10 * i/10)) * (i + 1)))
        return self.l_e_list