7.Write a Python program to shuffle and print a specified list.

In [97]:
import random
test_list=[3,4,5,6,7]
print("original list is:",test_list)
random.shuffle(test_list)
print("after shuffled list is:",test_list)