import random
import string


class Robot:
    def __init__(self):
        self.name = self.name_asign()

    def name_asign(self):
        rnd_name = ''
        for i in range(2):
            rnd_name += random.choice(string.ascii_uppercase)
        for j in range(3):
            rnd_name += str(random.choice(range(10)))
        return rnd_name

    def reset(self):
        random.seed()
        self.name = self.name_asign()
