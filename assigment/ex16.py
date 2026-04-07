#16.Counting the frequencies in a list using a dictionary in Python.
#Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
#Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

numbers=[1,1,1,5,5,3,1,3,3,4,4,4,2,2]
dic={}
for i in numbers:
    dic[i]=numbers.count(i)
print(dic)