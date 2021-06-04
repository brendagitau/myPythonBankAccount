class Gari:
    type="MERCEDES"
    def __init__(self,model,color,engine,capacity):
        self.model=model
        self.color=color
        self.engine=engine
        self.capacity=capacity
    def accelerate(self):
        return f"This is the {self.model} by the {self.type} company.It has an engine capacity of {self.engine} that enables  it accelerate at: Acceleration 0–100 km/h in	5.3 seconds"

    def  self_drive(self):
        return f"The version presented is {self.color} in color and has the capacity of{self.capacity}"      