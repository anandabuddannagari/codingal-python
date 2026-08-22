#Part 1: Define a function with no arguements to greet the customer
def greet_customer():
    print("Welcome to the lemonade Stand!")
    print("Fresh lemonade, made just for you.")

#PART 2: Call the greet_customer function
greet_customer()

#PART 3: Ask for the price per cup and the number of cup sold
price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold:"))

#PART 4: Define a function thats takes arguements and returns the total cost
def calculate_total(price, cups):
    total = price * cups
    return total
#PART 5: Call calculate_total and store the value it returns
total_cost = calculate_total(price_per_cup, cups_sold)

#PART 6: Use a built- in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Total cost:", rounded_total)

# PART 7: Ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer:"))
#Part 8: Define a function that takes arguements and returns the change due
def calculate_change(paid, total):
    change = paid = - total
    return change
#PART 9: Call calculate_change and store the value it returns
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

#Part 10: Define a function that returns a thank you message based on cups sold
def thank_you_message(cups):
    if cups >=5:
        return" wow, big order! Thanks so much for your support!"
    else:
        return"Thanks for stoppping by the stand"

#PART 11: Call thank_you_message and store the value it returns
closing_message = thank_you_message(cups_sold)

#Part 12 print the final lemonade stand receipt
print("")
print("====LEMONADE STAND RECEIPT =====")
print("Price per cup:", price_per_cup)
print("cup sold:",cups_sold)
print("total cost:", rounded_total)
print("Amount paid:", amount_paid)
print("change due:",rounded_change)
print(closing_message)
print("======================================================")
