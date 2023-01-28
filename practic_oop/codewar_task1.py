#Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).



#The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value
#The code you provided is a correct implementation of the function to sum all the numbers in an array, except for the highest and lowest elements. The function first sorts the array using the sorted() function, then uses slicing to exclude the first and the last
#
#

def sum_array(arr):

    #your code here

    return sum(sorted(arr)[1:-1]) if arr else 0
