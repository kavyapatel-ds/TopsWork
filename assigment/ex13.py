#13.Write a Python program to sort a dictionary (ascending /descending) by value
data = {'a':'apple','b':'cherry','c':'banana'}
# ascending order
print(sorted(data.values()))

#Desceding order
print(sorted(data.values(),reverse=True))