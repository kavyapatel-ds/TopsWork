# 19.Write a Python function that takes a list and returns a new list with unique 
# elements of the first list

def unique_list(lst):
    result=[]
    for i in lst:
        if i not in result:
            result.append(i)
    return result
numbers=[1,2,2,3,4,4,5]
print(unique_list(numbers))