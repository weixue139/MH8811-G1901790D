#Program C2 -transform C1 into function, and write and apply max , average , median , range function

#define the list
L=[9, 41, 12, 3, 74, 15]

#define function to find min of the numbers in C1
def my_min():
#initialize with None
    min_so_far = None
    for the_num in L:
        if min_so_far is None:
            min_so_far = the_num
            continue
        if the_num < min_so_far:
            min_so_far = the_num
    return min_so_far

#define function to find max of the numbers in C1
def my_max():
#initialize with None
    max_so_far = None
    for the_num in L:
        if max_so_far is None:
            max_so_far = the_num
            continue
        if the_num > max_so_far:
            max_so_far = the_num
    return max_so_far
     
#define function to find the average
def my_average():
    
    count=0
    sum=0
    for value in L:
        count=count+1
        sum=sum + value
    
    #return and round the average to 3 decimal places
    return round(sum/count,3)

#define function to find the median
def my_median():
    L.sort()
    len(L)
    r=int(len(L)/2)
 
    #to check the reminder of the length, and use condition to assign median value
    if len(L)%2 !=0:
        med=L[r-1]
    if len(L)%2 ==0:
        med=(L[r-1]+L[r])/2
   
    return med

#define function to find the range, use function of max and min here
def my_range():
    range1=my_max()-my_min()
    return range1
  

print('The list is', L)
print('The min is:',my_min())
print('The max is:',my_max())
print('The average is:', my_average())