numbers = [1, 2 ,3]
#new_numbers = [new_item for item in list]
new_numbers = [n + 1 for n in numbers]

name = "Jipara"
new = [letter for letter in name]

new_range = [n * 2 for n in range(1, 5)]

names = []
short_names = [name for name in names if len(name) < 5]

short_names = [name.upper() for name in names if len(name) < 5]
