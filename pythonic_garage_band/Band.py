from abc import abstractclassmethod

"""class will be inherited to kind of musician"""
class Musician:
 
    members = []

    def __init__(self, name):

        self.name = name
        Musician.members.append(self)

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass

""" sub class of musician that can play guitar """
class Guitarist(Musician):

    def __str__(self):

        return "My name is {} and I play guitar".format(self.name)

    def __repr__(self):

        return "Guitarist instance. Name = {}".format(self.name)

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

""" sub class of musician that can play drummer """
class Drummer(Musician):
    def __str__(self):

        return "My name is {} and I play drums".format(self.name)

    def __repr__(self):

        return "Drummer instance. Name = {}".format(self.name)

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

""" sub class of musician that can play Bassist """
class Bassist(Musician):
    def __str__(self):

        return "My name is {} and I play bass".format(self.name)

    def __repr__(self):

        return "Bassist instance. Name = {}".format(self.name)

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

""" create class  band from provided musicians"""
class Band(Musician):
    def __init__(self, name, members):

        self.name = name
        self.members = members
        Band.instances.append(self.name)
    def __str__(self):
        return f'My name is: {self.name}'
    def __repr__ (self):
         return (f"Band instance. Name = {self.name}")

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances