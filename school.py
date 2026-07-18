print("===Smart School Day Planner===")
print("Answer 3 quick questions and I will plan your day!/n")

day   = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather?(Sunny/ rainy/cloudy):").strip().lower()
homework = input("IS your homework done?(Yes/ no):").strip().lower()

print()
print(f"=== Your Plan for {day}===")
print("-" * 35)

#Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    :Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type      : First day of the week. Pack your weekly planner.")
elif day =="Friday":
    print("Day type     : Last school day.return libary books today.")
elif day in ("tuesday", "Wednesday", "Thrusday"):
    print("Day type   : Regular school day. Stay focused!")
else:
    print("Day tyoe  : day not recognised. Please check the spelling.")

#Topic 2 -- AND operator:sunny and homework done
if weather == "sunny" and homework =="yes":
    print("After school: Head the park - great weather and homework is done!")

#Topic 3 -- OR operator:rainly or cloudly
if weather == "rainy"or weather == "cloudly":
    print("Weather tip ; pack your umbrella - it may get wet outside.")

#topic 4 --NOT operator: homework NOT donw
if not(homework == "yes"):
    print("Homework  : Not done yet. Finish it before going out!")

#topic 5 -- Combining AND+ OR + NOT together
if weather == "rainy" and not (homework == "yes"):
    print("Best plan   :Stay in,finish homework, then watch your favourite show.")
elif weather =="sunny" and homework == "yes" and not (day in ("saturday", "Sunday")):
    print("best plan  : ALL set for a great school day - you are prepared!")
elif day in ("Saturday","sunday") and weather == "sunny":
    print("best plan : perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this")

print()
print("Plan complete! Have a wonderful day!")
