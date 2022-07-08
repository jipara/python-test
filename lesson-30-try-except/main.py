#FileNotFound

try:
    file = open("day-30.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    open("day-30.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"This key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")
    # file.close()
    # print("file was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("This is not human height")

bmi = weight / height ** 2
print(bmi)
