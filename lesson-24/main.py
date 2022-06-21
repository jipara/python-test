PLACEHOLDER = "[name]"
import os
# with open("/Users/mymacbook/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
#     print(names.read())
#     # names.read()
#     # print(names.readlines())
with open("/Users/mymacbook/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("/Users/mymacbook/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)









# letter = open("/Users/mymacbook/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r")
# for line in open("/Users/mymacbook/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt"):
#     line = line.replace("[name]", x[7])
#     text = "\n"
#     line.strip("\n")
#     print(line)
# letter.close()
