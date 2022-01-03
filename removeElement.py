nums = [3, 2, 2, 3]
val = 3

for i in range(len(nums)):
    if nums[i] == val:
        nums[i] = 52

c = 0
for n in nums:
    if n <= 50:
        c += 1
nums.sort()
print("c:", c, ", nums:", nums)
