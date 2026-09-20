#PART 1: Create two fruit baskets as sets
basket1 = {"apple","banana","mango","apple","grape"}
basket2 = {"mango","kiwi","banana","kiwi"}
print("Basket 1:", basket1)
print("Basket 2:",basket2)

#Part 2: Add a new fruit to basket1
basket1.add("orange")
print("Basket 1 after adding orange:", basket1)

#Part 3: Find fruits common to both baskets
common_fruits = basket1.intersection(basket2)
print("fruits in both baskets:",common_fruits)

#Part 4: Create an array of fruit counts using the array module
import array as arr
fruit_counts = arr.array('i',[3,5,2,4])
print("Fruits counts array:",fruit_counts)

#Part 6: Count how many times the number 4 appears in array
fruit_counts.reverse()
print("Reversed fruit counts array:",fruit_counts)

#Part 8: print thr final class fruit basket organizer summart

print("")
print("====CLASS FRUIT BASKET ORGANIZER====")
print("Basket 1:", basket1)
print("Basket 2:",basket2)
print("Shared fruits:",common_fruits)
print("Fruit counts:",fruit_counts)
print("==========================================================================================")