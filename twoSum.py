nums=[2,7,11,15]
target = 9
# Using One pass = Hashmap (Dictionary)
def sum_onePass(nums, target):
    index_dic={}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_dic:
            return [ index_dic[complement], i]
        index_dic[num] = i
        print(index_dic[num])
    return None
print(sum_onePass(nums, target))


# ..............Using brutforce..................
# def sum_brut_force(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
            

#         return None
# print(sum_brut_force(nums, target))

