#Assignment2 Program2- prompts user to input temperature in Celsius and outputs it in Fahrenheit
#C=input('Please type temperature in Celsius:')
c=input('Please type temperature in Celsius:')

#convert type str to float
C=float(c)

#formula to convert Celsius to Fahrenheit
F=1.8*C + 32

#round F into 3 decimal places to avoid unnecessasry display of too much decimal places due to float 
Output_F=round(F,3)

#print the output in Fahrenheit
print('The corresponding temperature in Fahrenheit is', Output_F)