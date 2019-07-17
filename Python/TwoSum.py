
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums.sort()
    i = 0
    j = len(nums) - 1
    while nums[i] + nums[j] != target:
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return [i,j]


if __name__ == "__main__":
    num = [1,2,5,3,8]
    target = 7
    twoSum(num, target)
