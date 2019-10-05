#Program C1 to find smallest number

#define the list
L=[9, 41, 12, 3, 74, 15]

#initialize with Noun
smallest_so_far = None
for the_num in L:
    if smallest_so_far is None:
        smallest_so_far = the_num
        continue
    if the_num < smallest_so_far:
        smallest_so_far= the_num
   
#print the list and the smallest number found in the program
print('The list is', L)
print('The minimum value is: ', smallest_so_far)