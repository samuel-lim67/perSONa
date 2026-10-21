#test test
class Character:
    def __int__(self,name,max_hp,defense):
        self.name=name
        self.max_hp=max_hp
        self.current_hp=max_hp #initial health should be full unless we chain battles
        self.defense = defense 