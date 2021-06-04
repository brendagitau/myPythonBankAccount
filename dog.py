class Doggie:
    type="Man's best friend"
    def __init__(self,name,breed,color,coat):
        self.name=name
        self.breed=breed
        self.color=color
        self.coat=coat
    def bark(self):
        return f"Hi there  my name is {self.name} and I am a {self.breed}.I howl at the moon alot."  
    def play (self):
        return f"I have {self.color} and {self.coat}"      