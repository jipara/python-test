def turn_right():
    turn_left()
    turn_left()
    turn_left()



for i in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
############
# while at_goal != True:
#     jump()
    
##########
#while not at_goal():
   # jump()

#########
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
