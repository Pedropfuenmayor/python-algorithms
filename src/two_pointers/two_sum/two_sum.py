"""
Given a sorted array of integers nums, 
determine if there exists a pair of numbers that sum to a given target.

Examples:
    Input: nums = [1,3,4,6,8,10,13], target = 13
    Output: True (3 + 10 = 13)

    Input: nums = [1,3,4,6,8,10,13], target = 6 
    Output: False
"""


def two_sum_v1(nums, target):
    """
    Time Complexity: O(n²) - uses nested loops to check all pairs
    Space Complexity: O(1) - uses constant extra space
    """
    first_idx = 0
    last_idx = len(nums)

    for outer_idx in range(first_idx, last_idx):
        inner_start_idx = outer_idx + 1
        for inner_idx in range(inner_start_idx, last_idx):
            if nums[outer_idx] + nums[inner_idx] == target:
                return True

    return False


def two_sum_v2(nums, target):
    """
    Time Complexity: O(n) - uses two pointers to traverse the array once
    Space Complexity: O(1) - uses constant extra space
    """
    if len(nums) < 2:
        return False

    if nums[0] + nums[1] > target:
        return False

    if nums[len(nums) - 1] + nums[len(nums) - 2] < target:
        return False

    left_index = 0
    right_index = len(nums) - 1

    while left_index < right_index:
        total_sum = nums[right_index] + nums[left_index]

        if total_sum == target:
            return True

        elif total_sum < target:
            left_index += 1

        elif total_sum > target:
            right_index -= 1

    return False


if __name__ == "__main__":
    print(f"Result: {two_sum_v2([1,3,4,6,8,10,13], 13)}")
