numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if not num % 2]
#or
result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

print(result)


####

with open("file1.txt") as file1:
  list_file1 = file1.readlines()

with open("file2.txt") as file2:
  list_file2 = file2.readlines()  

result = [int(n.strip()) for n in list_file1 if n in list_file2]

# Write your code above 👆

print(result)
