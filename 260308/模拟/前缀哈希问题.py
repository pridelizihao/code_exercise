# def twosum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             x, y = nums[i], nums[j]
#             if x + y == target:
#                 return [i,j]

def twosum(nums, target):
    dict1 = {}
    for i,x in enumerate(nums):
        if dict1.get(target -x) is not None:
            return [i, dict1[target-x]]
        dict1[x] = i
