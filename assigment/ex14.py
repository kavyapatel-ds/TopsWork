#14.Write a Python program to find the highest 3 values in a dictionary
scores={'a':50,'b':69,'c':30,'d':90,'e':60}
values=scores.values()
sorted_values=sorted(values,reverse=True)
result=sorted_values[:3]
print("tops 3 values",result)