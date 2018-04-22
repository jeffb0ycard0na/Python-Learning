# add to the program below so that if it finds a meal without spam
# if prints out each of the ingredients of the meal.
# You will need to setup the menu as did in lines 5-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "bacon", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", 'spam"'])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if not "spam" in meal:
        # print(meal)
        for ingredient in meal:
            print(ingredient)