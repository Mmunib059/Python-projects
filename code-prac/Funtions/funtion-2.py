# WAF to print the elements of a list in a single line. ( list is the parameter)

cities ={"kashmir", "islamabad", "lahore"}

def dis_list(list):
    for item in list:
        print(item, end=" ")
        
    print(len(list))
    
dis_list(cities)
