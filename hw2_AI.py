

# Thomas Schaeffer
# CISC681 - AI
# Homework 2: 'Alpha Beta Pruning' 
# 10/15/23

#You need to write a program that receives 12 numbers separated by space from the user. 
#The 12 input numbers will correspond to the 12 terminal nodes of the tree from left to right. 
#Your program should print the index of the terminal states that will be pruned using the alpha-beta search algorithm. 

# Resuources:
# [1] https://github.com/morgankenyon/RandomML/blob/master/src/minimax.py#L15
# [2] https://www.geeksforgeeks.org/python-integers-string-to-integer-list/


#[1]: tree print function shows problem struct



import sys

# -------- BUILD TREE ----------
input  = input()

# [2]: extract leaf ints from input
leaf_vals = [int(ele) for ele in input.split()]


# left most branch
max1 = max(leaf_vals[0:2])
min1 = max1
if leaf_vals[2] >= min1:
    sys.stdout.write('3 ')
  
else:
    max2 = max(leaf_vals[2:4])
    min1 = min(max1,max2)

root = min1

# middle branch
max3 = max(leaf_vals[4:6])
min2 = root
if max3 <= min2:
    sys.stdout.write('6 7 ')
elif leaf_vals[6]>=max3:
    sys.stdout.write('7 ')
    min2 = max3
else:
    max4 = max(leaf_vals[6:8])
    min2 = min(max3,max4)
    root  = max(min1,min2)



# right branch
min3 = root
max5 = max(leaf_vals[8:10])
if max5 <= root:
    sys.stdout.write('10 11 ')
elif leaf_vals[10] >= max5:
    sys.stdout.write('11 ')
    min3 = max5
else:
    max6 = max(leaf_vals[10:12])
    min3 = min(max5,max6)

root = max(min1,min2,min3)




