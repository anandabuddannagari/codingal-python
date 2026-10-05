#create class
class Vehicle:

    #create init method
    def __init__(self, max_speed, mileage):

        #bind the arguements 
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX = Vehicle(240,18)

#Access the variables inside init mehod
print("Model max speed:",modelX.max_speed)
print("Model Mileage",modelX.mileage)