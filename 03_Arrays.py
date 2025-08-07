'''arrays -> An array can be defined as a storage or container or similar items placed in contiguous memory location. These elements can be of any datatypes'''

arr1 = [1,2,3,4,5,6]
arr2 = [1.2,4.5,6.4,1.6]
arr3 = ['a', 'b','c', 'd', 'e']

# printing type of an array
print(set(type(x) for x in arr1))
print(set(type(x) for x in arr2))
print(set(type(x) for x in arr3))

# printing the number of elements in an array

# for i in range(0, len(arr1)):
#     print(arr1[i], end= ' ')
print(*arr1)
print("\n")

for i in range(0, len(arr2)):
    print(arr2[i], end=', ' )
print("\n") 

for i in range(0, len(arr3)):
    print(arr3[i], end= ' ')
print("\n")

# assessing elements from an array using index values

import array 

arr3 = array.array('i', [10,20,30,40,50])
print(arr3[4])

# adding elements in an array

arr3.insert(0,2)
arr3.append(60)

print(*arr3)

# updating elements in an array

new_array = array.array('i', [20,40,60,80,100])
new_array[2] = 50
print(*new_array)

#deleting elements from an array

new_array.pop(3)
print(*new_array)
new_array[3] = 80
new_array.append(100)

print(*new_array)

# deleting elements from an array

new_array.remove(50)
print(*new_array)

# slicing 

x = list(range(0,100,3))
arr5 = array.array('i', x)

print(list(arr5))

arr0 = arr5[10:-10]
print(list(arr0))   

# searching 

x = list(range(0, 1000,4))
search_array = array.array('i', x)

if 400 in search_array:
    print(search_array.index(400))
else:
    print("nothing found")

# for searching multiple values 
targets = [100, 250, 400, 999]

for i in targets:
    if i in search_array:
        print(f"{i} found at index {search_array.index(i)}")
    else:
        print(f"{i} not found")


# sorting 

sort_array = array.array('i', [5,4,6,7,8,9,2,3])
sort_array = sort_array.tolist()

# in ascending order
sort_array.sort()
print(list(sort_array))

# in descending order

sort_array.sort(reverse= True)
print(list(sort_array))




