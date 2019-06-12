#Treeshan Yeadram
#Oct 22,2018
#This program prints the poplution.


#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

user= input("Enter Borough Name: ")
filename= input("Enter an OutPut File: ")
#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[user]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')
 
#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(filename)
