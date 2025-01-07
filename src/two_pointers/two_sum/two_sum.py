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
    first_idx = 0
    last_idx = len(nums)

    for outer_idx in range(first_idx, last_idx):
        inner_start_idx = outer_idx + 1
        for inner_idx in range(inner_start_idx, last_idx):
            if nums[outer_idx] + nums[inner_idx] == target:
                return True

    return False


if __name__ == "__main__":
    print(f"Result: {two_sum_v1([1,3,4,6,8,10,13], 13)}")
