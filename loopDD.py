#Treeshan YEadram



#Sample program that loops from 10 down to 0
ADDI $s0, $zero, 0 #set s0 to 10
ADDI $s1, $zero, 10 #use to decrement counter, $s0
ADDI $s2, $zero, 100
AGAIN: ADD $s0, $s0, $s1
BEQ $s2, $s0, DONE
J AGAIN
DONE:  #To break out of the loop
