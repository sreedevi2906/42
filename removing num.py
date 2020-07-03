5.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

In [76]:
l1=[1,3,5,7,9,10,12]
l1=[x for (i,x) in enumerate(l1)if i not in (0,4,5)] 
print(l1)