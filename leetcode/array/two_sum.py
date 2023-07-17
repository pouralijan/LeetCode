def twoSum(nums, target):
    """
    nums = [2,7,11,15], target = 9


    abs()
    9 - 2  -> 7
    9 - 7  -> 2
    9 - 11 -> -2
    """

    checked = {}
    for index, num in enumerate(nums):
        diff = abs(target - num)

        if diff in checked:
            return [checked[diff], index]
        checked[num] = index

print(twoSum([2,7,11,15], 9))