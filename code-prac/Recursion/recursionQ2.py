# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def dis_list(list, ind=0):
    if ind == len(list):
        return
    print(list[ind])
    dis_list(list, ind+1)
    
color=["kela", "neela","surkh"]

dis_list(color)
