def majority_element(nums):
    """
        [2,2,1,1,1,2,2]
    """
    statistics = {}
    majority = nums[0]
    for element in nums:
        if element in statistics:
            statistics[element] += 1
            if statistics[element] > len(nums)/2:
                majority = element
        else:
            statistics[element] = 1
    return majority

print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([3, 2, 3]))
print(majority_element([6,5,5]))