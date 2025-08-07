'''Time complexity -> measures how the running time of an algorithm changes as the size of its input data grows. Rate of increase of time with respect to input size.'''

n = int(input('How many times you want to print it: '))
for i in range (1 , n+1):
    print("Tushar Choudhary") # time complexity Big O Notation -> O(n)


# Case scenrio
age = int(input("enter your age:  "))

if age >= 80:
    print("senior citizens")

elif age >=60:
    print("senior")

elif age >=24 and age<60:
    print("working people")

elif age >=16 and age< 24:
    print("teen")

else:
    print("baby") 

# here the best case is when we put age somewhere above 80, so that it can only run 2 operations and the worst case is when we put age below 16. Always find Time complexity in worst case scenrio.



# Avoiding constant values and avoiding lower values

'''Time complexity -> O(8N^6 + 3N^2 + 15) and let N = 10^15
                      O(8*10^30 + 3*10^10 + 15), here 15 is neglected, Because We Focus on Growth, Not Exact Count and Constants Don't Change the Growth Pattern
                      O(8*10^30 + 3*10^10)
                      O(8*10^30), here '3*10^10', because they don't affect the growth rate and also small inputs always run fast anyway
                      O(N^6)-> time complexity and 8 is also negelected because again it is a constant value and also we just want to give rate.'''
                      

# example 1-> find the time complexity 

for i in range (1, n+1):
    for j in range(1, n+1):
        print()   # time complexity of this will be O(N^2)

# example 2 -> find the time complexity

for i in range (1, n+1):
    for j in range(1, i+1):
        print() # time complexity of this becomes n(n+1)/2, and after futher simplfying it, it will becomes n^2, so this will become O(n^2).


'''Space Complexity -> It is the memory space required by an algorithm until it executes completely.  Space Complexity = Auxiliary Space + Input Space'''
# Auxiliary space -> The extra space used to solve the problem.
# Input space -> The space used to store the input and solving the problem.

# example -> add 3 numbers and then print there total

a = 45
b = 34
c = 55

total = a+b+c
print(total)   # here input space is where we stored the values of a,b,c and the auxiliary space is that where we stored total sum of a,b and c



