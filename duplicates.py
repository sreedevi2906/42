2.Write a Python program to remove duplicates from a list.

In [10]:
mylist=[2,5,5,6,6,9,3]
prev=None
newlist=[]
for item in mylist:
  if item!=prev:
        newlist.append(item)
        prev=item
print("The new list:\n")
print(newlist)