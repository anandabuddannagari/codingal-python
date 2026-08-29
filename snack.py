#snack Vending Machine

#PART 1: A function that works out change and sents it back with return
def calculate_change(paid, price):
    change=paid-price
    return change

#Part 2: set the snake price and greet other customers
snack_price = 25
print("====SNACK VENDING MACHINE =====")
print(f"this snack costs{snack_price}units. ")
print("Accepted coins:1,5,10,25\n")

total_inserted =0
coins_inserted = 0

#PART 3: Keep accepting coins until enough money is inserted
while True:
    coin = int(input("Insert a coins(1,5,10, or 25)"))

    #PART 4: Reject any coin that isnt a valid value
    if coin !=1 and coin !=5 and coin !=10 and coin !=25:
        print("Invalid coin, try again!\n")
        continue

    #Part 5: add the valid coin to the running total
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    #Part 6:stop asking for coins once enough has been inserted
    if total_inserted >=snack_price:
        print("Enough Money inserted!\n")
        break

    #Part 7:work out the change using the caluse returned by calculate_change
    change_due = calculate_change(total_inserted, snack_price)

    print("Dispensing your snack...")
    #Part 8:Nothing Extra to do when the change is exactly zero
    if change_due ==0:
        pass
    else:
        print(f"Here is your change:{change_due}units")

    #Part 9:Print a short summary of the purchase
    print("\n====PURCHASE SUMMARY ====")
    print("snack price:", snack_price)
    print("Coins inserted:", coins_inserted)
    print("total paid:", total_inserted)
    print("change Given:", change_due)
    print("Thanks for your purchase!")

    #End of the PROGRAM