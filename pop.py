#Treeshan Yeadram
#Oct 22,2018
#Print poplution

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter a name of a Borough: ")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)

print("The average population is : " , pop[borough].mean())

print("The Maximum population is: ", pop[borough].max())
