# 8.Write a Python program to check whether a list contains a sublist.
main_list=[1,2,3,4,5]
sub_list=[3,4]
if sub_list[0]in main_list and sub_list[1] in main_list:
    print("sublist present")
else:
    print("sublist not present")