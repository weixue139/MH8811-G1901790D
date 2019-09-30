#P03 transform the previous 3 programs into functions and ask user to choose program to execute, with an exit option
#print the descriptions of choices
print("Choose the sub-programs by input 1, 2 or 3")
print("1 will display 'Hello, world!'")
print("2 will ask you to input your name and display 'Hello, <your name>!'")
print("3 will ask you to input a temperature in Celsius then display the temperature in Fahrenheit")

#define the 3 functions
def func1():
    print("Hello, world!")

def func2():
    name=input("What is your name?")
    print('Hello,', name,'!')
    
def func3():
    #ask user to input temperature
    c=input('Please type temperature in Celsius:')

    #convert type str to float
    C=float(c)

    #formula to convert Celsius to Fahrenheit
    F=1.8*C + 32

    #round F into 3 decimal places 
    Output_F=round(F,3)

    #display the output in Fahrenheit
    print('The corresponding temperature in Fahrenheit is', Output_F)


#use while loop to choose which function to run with an exit option
while True:
    #ask user input choice and use conditions to call the function
    choice=input("Please input a number 1, 2 or 3 to choose your sub-program, 4 to quit:")
    choice=int(choice)
    if choice==1:
        func1()    
    elif choice==2:
        func2()
    elif choice==3:
        func3()
    #if input is 4, use break to exit the loop
    elif choice==4:
        print('Finished')
        break
    
    else:
        #ask user to input again if did not input a valid choice earlier
        print ('Not a valid choice, please choose again by type 1, 2, 3 only, 4 to quit:')

    