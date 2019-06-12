#Name: ...Sakib Ahmad...
#Date: September 5, 2018
#This program implements the psuedocode

#Import the turtle commands to use below:
import turtle

#Create a turtle, named: star
star = turtle.Turtle()

#Repeat 36 times:
for i in range(36):
    star.forward(100)   #Move star forward 100 steps
    star.left(145)  #Turn star 145 degrees to the left
    star.forward(10)    #Move star forward 10 steps
    star.right(90)  #Turn star right 90 degrees to the right
    star.forward(10)    #Move star forward 10 steps
    star.left(135)  #Turn star to the left 135 degrees
    star.forward(100)   #Move star forward 100 steps


