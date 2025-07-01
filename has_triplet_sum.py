def has_triplet_sum(nums: list[int], target: int) -> bool:
    i = 0
    while i < len(nums):
        j = 0
        while j < len(nums):
            k = 0
            while k < len(nums):
                if nums[i] + nums[j] + nums[k] == target:
                    return True
                k += 1
            j += 1
        i += 1
    # If no triplet found, return False
    return False

print(has_triplet_sum([4, 3, 3], 6))