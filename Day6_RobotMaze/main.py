
#online python course
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left() 
             
def check_side():
    if wall_in_front() == True:
       if wall_on_right() == True:
           if wall_in_front() == True:
               turn_left()
       elif wall_in_front() == False:
           move()
        
       else:
           turn_right()
            
    elif wall_in_front() == False:
        move()
        if wall_on_right() == False:
            turn_right()
        if wall_on_right() == True:
            turn_left()
    
    else:
        turn_right()
         
while not at_goal():
    check_side()