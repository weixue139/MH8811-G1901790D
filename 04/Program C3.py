#Program C3 Use getFineLines function, calculate and output statistics

#define getFileLines function
def getFileLines(fname) :
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    fhandle.close()
    return lines

#run the function to a file
L = getFileLines(r'C:\Users\WX\Documents\NTU FinTech\Python\Python Assignment\04\MH8811-04-Data.csv')

#convert string to integer
L =[int(i) for i in L]

#define function to find min of the numbers
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

#define function to find max of the numbers
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
        med=L[r]
    if len(L)%2 ==0:
        med=(L[r-1]+L[r])/2
 
    return med
    
#define function to find the range, use function of max and min here
def my_range():
    range1=my_max()-my_min()
    return range1
  
#output the statistics
print('The average is:', my_average())
print('The min is:',my_min())
print('The max is:',my_max())
print('The median is:',my_median())
print('The range is:',my_range())
