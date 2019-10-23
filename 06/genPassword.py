#06 Homework H1 module by Wei Xue

#Module to generate a strong password of length n (n>=4):
#import necessary modules:
import string
import random

#Function to generate a strong password of length n (n>=4):
def genPassword(n):
    #define variables to contain the groups of symbols:
    #lowercase letters:
    let_low = string.ascii_lowercase
    #uppercase letters:
    let_upp = string.ascii_uppercase
    #numbers (digits):
    num = string.digits
    #special symbols:
    symb = string.punctuation
    #group containing all symbols:
    symb_all = let_low + let_upp + num + symb
    
    #pick at least one symbol from each group:
    password = random.choice(let_low) + random.choice(let_upp) + random.choice(num) + random.choice(symb)
    
    #pick the remaining symbol(s) if any:
    for i in range(n-4):
        password += random.choice(symb_all)
    
    #convert password string into a list and reshuffle the order of the list in place:
    password_list = list(password)
    random.shuffle(password_list)
    
    #convert the shuffled list of symbols back to a string:
    password = ''.join(password_list)
    
    #return final password as a string
    return password

#If the module is run as a main program:
if __name__ == "__main__":
    #output a password of length 12:
    password = genPassword(12)    
    print('The generated strong password of length 12 is: ' + password)
    