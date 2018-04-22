# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.


name = input("What is your name? ")
age = int(input("How old are you? "))

if (age >= 18) and (age <= 30):
    print("Welcome the the holiday party!")
else:
    print("I'm sorry but you aren't in the appropriate age group")
