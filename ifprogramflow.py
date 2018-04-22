# #Example1
# name = input("Please enter your name: ")
# age = int(input("how old are you, {0}".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

# #Example2
# # print("Please pick a number between 1 and 10: ")
# # guess = int(input())
# #
# # if guess != 5:
# #     if guess < 5:
# #         print("Please guess higher")
# #     else:
# #         print("please guess lower")
# #     guess = int(input())
# #     if guess == 5:
# #         print("Well done, you guess it")
# #     else:
# #         print("Sorry, you have not guessed correctly")
# # else:
# #     print("You got it on your first try")

# #Example3 use paranthese to be more explicite
# age = int(input("How old are you? "))
#
# if (age >= 16) and (age <= 65):
#     print("Have a good day at work")

# #Example 4
# age = int(input("How old are you? "))
#
# if 16 <= age <= 65:
#     print("Have a good day at work")

# #Example 5
# age = int(input("How old are you? "))
#
# if 15 < age < 66:
#     print("Have a good day at work")

# #Exmaple 6
# age = int(input("How old are you? "))
#
# if (age < 15) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# #Example 7
# x = "false"
# if x:
#     print("x is true")

# # Example 8
# x = input(" Please enter some text ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

# # Example 9
# print(not False)
# print(not True)

# # Example 10
# age = int(input("How old are you? "))
# if not(age < 18):
#     print("yYou are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back {0} years".format(18-age))

# # Example 11 Searching for characters in parrot which is "Norwegian Blue"
# parrot = "Norwegian Blue"
#
# letter = input("Enter a character: ")
#
# if letter in parrot:
#     print("Give me an {}, Bob".format(letter))
# else:
#     print("I don't need that letter")
