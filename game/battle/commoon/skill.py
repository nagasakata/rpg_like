from game.character.common.character import Character


class Skill():
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name