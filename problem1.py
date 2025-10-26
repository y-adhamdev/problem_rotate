def reverse(nums:list, i:int, j:int) -> list:
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums

def rotate(nums: list, k: int) -> list:
    k = k % len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)

    return nums
    
