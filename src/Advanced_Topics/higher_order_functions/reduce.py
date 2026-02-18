from functools import reduce
nums=[2,3,4,5]
sum=reduce(lambda x,y: x+y,nums)
print(sum)

product=reduce(lambda x,y: x*y, nums)
print(product)

max_num=reduce(lambda x,y: x if x>y else y, nums)
print(max_num)
