'''Hashing -> It's a technique that efficiently stores data into some databases like Lists/dictonary/sets and and retrieves data in a way that allows for quick access. '''


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

x = max(n)

hash_list = [0] * (x+1)

for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num >  x:
        print (f"{num} : 0")

    else:
        print(f"{num} : {hash_list[num]}") # TC -> best/avg case => O(1) and in worst case => O(n) and SC -> O(1) 

# in this TLE error will not come because if elements in n = 10^8 and m = 10^8, then it will become 10^8 + 10^8 = 2*10^8, which becomes 10^8.


# using dictionary

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

dic = {}

for num in n:
    dic[num] = dic.get(num, 0) + 1

for num in m:
    print(f"{num} : {dic.get(num,0)}")    


# storing frequency in dictonary

# method 1

nums = [5,6,7,7,1,9,111,1,1,5,1,1]

n = len(nums)

dic = {}

for i in range(0,n):
    if nums[i] in dic:
        dic[nums[i]] += 1

    else:
        dic[nums[i]] = 1

print(dic) # TC -> best/avg => O(n), in worst => O(n^2), can be possible becuase of collision and SC -> O(n)

# method 2

nums = [5,6,7,7,1,9,111,1,1,5,1,1]

dic = {}

for i in range(0,n):
    dic[nums[i]] = dic.get(nums[i], 0) + 1

else:
    dic[nums[i]] = 1

print(dic)