nums = [int(x) for x in open('input', 'r').readlines()]
print(len(nums))
count = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1
print(count)
count = 0
for i in range(4, len(nums)):
    t1 = nums[i - 1] + nums[i - 2] + nums[i - 3]
    t2 = nums[i] + nums[i - 1] + nums[i - 2]
    if t2 > t1:
        count += 1
print(count)
