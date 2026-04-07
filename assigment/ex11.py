# 11.Write a Python program to unzip a list of tuples into individual lists.
data=[(1,'a'),(2,'b'),(3,'c')]
list1,list2=zip(*data)
print(list1)
print(list2)