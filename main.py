friend1 = "Ava - March 15"
friend2 = "Mia - July 12"
friend3 = "Noah - October 22"
friend4 = "Zara - January 9"
friend5 = "Leo - December 30"

print(friend1)
print(friend2)
print(friend3)
print(friend4)
print(friend5)

# Add this part so Python knows what 'birthdays' is
birthdays = {
    "Ava": "March 15",
    "Mia": "July 12",
    "Noah": "October 22",
    "Zara": "January 9",
    "Leo": "December 30"
}

print("\nBirthdays from dictionary:")
for name, bday in birthdays.items():
    print(name, ":", bday)
