# +ve-elements-in-list
# number of elements in list
n = int(input("Enter number of elements : ")) 

# Below line read inputs from user using map() function 
list1 = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 

for value in list1:
    if value>0 :
        print(value)
