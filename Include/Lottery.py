# This code will create enviroment lottery manager
class Lottery:
    
    enterprise = "lottery"

    def __init__(self, name, type):
        self.name = name
        self.type = type

lottery1 = Lottery("Bola Casas Lotericas", "Jogo do Bicho")

# acess lottery attributes
print("Enterprise is a {}".format(lottery1.__class__.enterprise), "\n")

# acess instance attributes
print("{} is this best beting house in the {}".format(lottery1.name,lottery1.type))
