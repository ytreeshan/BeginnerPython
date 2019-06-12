#Shania Gibson
#October 16,2018
#This program  a string as input and uses that string to control what the turtle draws on the screen

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()    
commands = input("Please enter a command string: ")

for ch in commands:
    if ch == 'F':           
        tess.forward(50)
    elif ch == 'L':        
        tess.left(90)
    elif ch == 'R':          
        tess.right(90)
    elif ch == '^':         
        tess.penup()
    elif ch == 'v':          
        tess.pendown()

    elif ch == 'B':            
        tess.backward(50)
    elif ch == 'S':         
        tess.stamp()
    elif ch == 'l':         
        tess.left(45)
    elif ch == 'r':         
        tess.right(45)
    elif ch == 'p':          
        tess.color("purple")
    else:                  
        print("Error: do not know the command:")

print("See graphics window for your image")
myWin.exitonclick()        
