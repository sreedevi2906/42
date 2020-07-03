3.Write a Python program to check a list is empty or not.

In [21]:
def Enquiry(lis1): 
 
    if len(lis1) == 0: 
 
        return 0
 
    else: 
 
        return 1
lis1 = [0,1,2] 
 
if Enquiry(lis1): 
 
    print ("The list is not empty") 
 
else: 
 
    print("Empty List")