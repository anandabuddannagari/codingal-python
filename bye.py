valid = False
while not valid: #valid nested while loop
    try:
        n=int(input("enter a number:"))
        #Enter a even number
        while n%2==0:

            print("bye")
        vaild=True
    except ValueError:
        print("invalid")