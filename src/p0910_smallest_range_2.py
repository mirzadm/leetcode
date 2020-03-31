"""Problem 910: Smallest range II."""

def smallest_range_2(nums, k):
    origin_min = min(nums)
    min_value = origin_min + k
    max_value = origin_min + k
    for num in nums:
        if num + k > max_value and num - k < min_value:
            if num + k - max_value > min_value - (num - k):
                min_value = num - k
            else:
                max_value = num + k
        elif num + k > max_value and num - k > max_value:
            max_value = num - k
    return max_value - min_value


if __name__ == "__main__":
    print(smallest_range_2([1, 3, 6], 3))
