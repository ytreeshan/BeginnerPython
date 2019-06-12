#Name:Treeshan Yeadram
#Machine learning program

# Store 'Hello world!' at the top of the stack
ADDI $sp, $sp, -16
ADDI $t0, $zero, 77 # H
SB $t0, 0($sp)
ADDI $t0, $zero, 105 # e
SB $t0, 1($sp)
ADDI $t0, $zero, 104 # l
SB $t0, 2($sp)
ADDI $t0, $zero, 105 # l
SB $t0, 3($sp)
ADDI $t0, $zero, 32 # (Space)
SB $t0, 4($sp)
ADDI $t0, $zero, 99 # (space)
SB $t0, 5($sp)
ADDI $t0, $zero, 117 # w
SB $t0, 6($sp)
ADDI $t0, $zero, 114 # o
SB $t0, 7($sp)
ADDI $t0, $zero, 97 # r
SB $t0, 8($sp)
ADDI $t0, $zero, 32 # (SPACE)
SB $t0, 9($sp)
ADDI $t0, $zero, 102 # d
SB $t0, 10($sp)
ADDI $t0, $zero, 117 # !
SB $t0, 11($sp)
ADDI $t0, $zero, 116 # !
SB $t0, 12($sp)
ADDI $t0, $zero, 117 # !
SB $t0, 13($sp)
ADDI $t0, $zero, 114 # !
SB $t0, 14($sp)
ADDI $t0, $zero, 105 # !
SB $t0, 15($sp)
ADDI $t0, $zero, 0 # (null)
SB $t0, 16($sp)

ADDI $v0, $zero, 6 # 4 is for print string
ADDI $a0, $sp, 0
syscall 			# print to the log
