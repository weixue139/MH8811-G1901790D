#06 Homework H1 main program by Wei Xue

#import the genPassword module:
import genPassword

#ask the user for length of password:
user_input = input('Please input the length of password to generate, for strong password, the length should be >= 4 to contain at least one lowercase letter, one uppercase letter, one number (digit), and one special symbol:\n')

try:
    password_len = int(user_input)
    if password_len < 4:
        print('Length is less than 4, aborting...')
    else:
        print('The generated strong password of length {} is: '.format(password_len), genPassword.genPassword(password_len))
except:
    print('Unrecognized Input!')