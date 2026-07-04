#input a word
text = str(input("enter a string:"))

#Reverse String
#using step va;ue as -1 to iterate in reverse
revText = text[ ::-1]
text = revText
print("Reverse of Given String is:")
print(text)