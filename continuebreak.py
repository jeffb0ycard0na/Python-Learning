# # Example 1
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == "spam":
#         break
#         # you can use "continue" to finish the list after skipping spam
#
#     print("Buy" + item)

# Example 2
meal = ["egg", "bacon", "spam", "sausage"]
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")
if nasty_food_item:
    print("Can't I have anything without spam in it")
