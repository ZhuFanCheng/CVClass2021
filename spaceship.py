import numpy as np
class spaceship:
    "Creates a class"
    def __init__(self,passengers,rest_mass):
        "Create a new color for each car part"
        self.hood = "Blue" 
        self.wheels = "Red"
        self.doors = "Green"
        self.passengers = passengers
        self.rest_mass = rest_mass
        self.c = 3e8
    def mass(self,speed):
        mass = self.rest_mass + self.passengers * 80
        final_mass = mass / np.sqrt(1-speed**2/self.c**2)
        return final_mass
    
spaceship = spaceship(10,1000)
speed = 3e8*0.99

final_mass = spaceship.mass(speed)

print("final mass is ", final_mass)  # Assign each point a unique location




