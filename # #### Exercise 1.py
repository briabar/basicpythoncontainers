# #### Exercise 1

# - Create a list named `students` containing some student names (strings).
# - Print out the second student's name.
# - Print out the last student's name.

students = ['Shlo', 'Shlimantha', 'Slimony', "Smangela"]
print(students[1])
print(students[-1])


# #### Exercise 2

# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
# - Use a `for` loop to print out the string "_food goes here_ is a good food".

foods = ('horse grits', 'toaster scrapings', 'hair melt', 'cheesy fermented bork')

for food in foods:
    print(food)

# #### Exercise 3

# - Using a `for` loop, print just the last two food strings from `foods`.

for food in foods[-2:]:
    print(food)
# #### Exercise 4

# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
# - Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"

home_town = {
    'city' : 'Chicago',
    'state' : 'Illinois',
    'population' : 9784838994949499,
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# #### Exercise 5

# - Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"

for item in home_town.items():
    print(f'{item[0]}: {item[1]}')

# #### Exercise 6

# - Create an empty list named `cohort`.
# - Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:

# 	```python
cohort = []
for i, student_name in enumerate(students):
    cohort.append({'student': student_name, 'fav_food': foods[i]})

print(cohort)
# 	```


# - Iterate over `cohort` printing out each element.

# #### Exercise 7

# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over `awesome_students` printing out each string.

awesome_students = [f'{x} is awesome!' for x in students]

for student_msg in awesome_students:
    print(student_msg)

# #### Exercise 8

# - Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.

print([x for x in foods if 'a' in x ])