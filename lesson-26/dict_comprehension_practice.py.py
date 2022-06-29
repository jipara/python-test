sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
def Convert(sentence):
    li = list(sentence.split(" "))
    return li
 
new_sentence = (Convert(sentence))

#or

new_sentence = sentence.split()

#or

result = {word:len(word) for word in sentence.split()}

result = {word:len(word) for word in new_sentence}


print(result)
