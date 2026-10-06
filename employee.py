#create class
class Employee:

    #Initalizing
    def __init__(self):
        print('Employee created')

        #calling destructor
    def __del__(self):
        print("Destructor called")

def create_obj():
    print('making object....')
    obj = Employee()
    print('function end......')
    return obj
    
print('Calling create_obj()function....')
obj = create_obj()
print('Program end....')