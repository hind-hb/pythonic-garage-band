from abc import ABC, abstractmethod

class Musician(ABC):

    def __init__(self, name):
        self.name = name
    @abstractmethod   
    def __str__(self):
        pass
    def __repr__(self):
        pass
    @abstractmethod
    def get_instrument (self):
        pass
    @abstractmethod
    def play_solo (self):
        pass

class Guitarist(Musician):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'My name is: {self.name}'
    def __repr__ (self):
         return (f"Guitarist instance. Name = {self.name}")
    def get_instrument (self):
        return "Guitar"
    def play_solo (self):
        return "Emotional Melodic Guitar Solo"

class Bassist(Musician):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'My name is: {self.name}'
    def __repr__ (self):
         return (f"Bassist instance. Name = {self.name}")
    def get_instrument (self):
        return "Bassist"
    def play_solo (self):
        return "Incredible Bass Solo"

class Drummer(Musician):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'My name is: {self.name}'
    def __repr__ (self):
         return (f"Drummer instance. Name = {self.name}")
    def get_instrument (self):
        return "Drummer"
    def play_solo (self):
        return "Benny Greb Drum Solo"

class Band(Musician):
    count = 0 
    instance = []
    def __init__(self,name,members=None):
        self.name=name
        self.member=members
        Band.instance.append(self)
    def __str__(self):
        return f'My name is: {self.name}'
    def __repr__ (self):
         return (f"Band instance. Name = {self.name}")
    def play_solo (self):   
        instance = []
        for so in self.solo:
            instance.append(so.play_solos()) 
        return instance
    @classmethod
    def to_list(cls):
         return cls.count



        
