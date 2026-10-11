#Class creation
class myClass:

    #private varibale
    __privateVar = 27;


    #private mehod
    def __privMeth(self):
        print("I am inside class myClass")


    #function to print value of private varibale
    def hello(self):
        print("Private Varibale value:", myClass.__privateVar)


#Objact creation and method call
foo = myClass()
foo.hello()
foo.__privMeth