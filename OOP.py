import json # used to formatting in output

class GTAplayer:
    def __init__(self, name, age, health, Skincolor, gender):
        self.name = name
        self.age = age
        self.health = health
        self.skincolor = Skincolor
        self.gender = gender

    def player_info(self, n, a, h, sC, g):
        data = {
            "player_name" : n,
            "player_age" :  a,
            "player_height" : h,
            "player_Skincolor" : sC,
            "player_gender" : g
        }

        return json.dumps(data, indent = 4)

p_1 = GTAplayer("Franklin", 32, 100.0, "black", "male")
result = p_1.player_info("Franklin", 32, 100.0, "black", "male")
print(result)