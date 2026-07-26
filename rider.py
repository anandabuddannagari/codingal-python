#Costom Ride Builder
#File : ride_builder.py
#Lessons: SPCM2L1 - Nested Conditional Statemnt


print("=================================")
print("     welcome to Ride Builder")
print("=================================")
print()

print("Step 1: Pick your vehicle")
print(" 1 - Bike")
print("  2 - Car")
print()

choice = int(input("Enter 1 or 2:"))
print()

if choice ==1:
    #nested if-else - runs only when choice is 1
    print("Step 2: Pick your bike type")
    print(" 1 - Scooty")
    print("   2 - Mountain Bike")
    print()
    bike_type= int(input("Enter 1 or 2: "))

    if bike_type ==1:
       print("You picked : Scooty")
       print("Top speed  : 80 km/h")
       print("Best for    :City roads")

    else:
        print("You picked  ; Mountain bike")
        print("Top speed  : 40 km/h")
        print("Best for   : off-road trails")

elif choice ==2:
    #Nested if-else - runs only when choice is 2
    print("STep 2: Pick your car type")
    print("  1 - Sedan")
    print("2 - Suv")
    print()

    car_type =int(input("Enter 1 or 2:"))
    print()

    if car_type ==1:
        print("You picked : Sedan")
        print("Seats     : 5 passengers")
        print("Best for   : Family trips")
    else:
        print("You picked : Suv")
        print("Seats     : 7 passengers")
        print("best for    : off-roads adventures")

else:
    print("Thats was not a vaild choice")
    print("Please eneter 1 for BIke of 2 for car")

print()
print("==================================")
print("     Your Costom ride is ready    ")
print("    Enjoy the journey             ")
print("=======================================")

