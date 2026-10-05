#create class
class Parrot:

    #class attribute
    species = "bird"

    #Instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age=age
    

#instaninate the parriot class
blu = Parrot("Blu",10)
woo=Parrot("Woo",15)


#acess thw class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))


#access the instance attributes
print("{}is{}years old".format(blu.name,blu.age))
print("{}is {}years old".format(woo.name,woo.age))