# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sumofNums = 0
count = 0 

for number in student_heights:
    sumofNums += number
    count += 1
average_number = round(sumofNums/count)
print(average_number)
