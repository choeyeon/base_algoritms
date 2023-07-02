nums = [5, 3, 9, 6, 3, 4, 6, 1, 4, 2, 6, 3, ]
print(nums)
swamp = True
while swamp:
    swamp = False

    for val in range(len(nums) -1):
        if nums[val] > nums[val + 1]:
            swamp = True
            nums[val], nums[val + 1] = nums[val +1], nums[val]

print(nums)