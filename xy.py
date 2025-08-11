
# 

nums = [27, 26, 48, 78, 2, 27, 27, 48, 26, 2, 2, 27, 48, 90]
n = len(nums)

dic = {}

for i in range(n):
    if nums[i] in dic:
        dic[nums[i]] +=1

    else:
        dic[nums[i]] = 1

print(dic)





    

