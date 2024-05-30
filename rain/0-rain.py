#!/usr/bin/python3
"""
Rainwater Retention
"""


def rain(walls):
    """
    Calculate the total amount of rainwater retained after rainfall.

    Args:
        walls (list): A list of non-negative integers representing the heights
                      of walls.

    Returns:
        int: Total amount of rainwater retained.

    Assumptions:
        - The ends of the list (before index 0 and after index walls[-1]) are
          not walls.
        - If the list is empty, return 0.
    """
    if not walls:
        return 0

    total_water = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    # Calculate the highest wall to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate the highest wall to the right of each wall
    right_max[-1] = walls[-1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the amount of water retained on each wall
    for i in range(len(walls)):
        total_water += max(0, min(left_max[i], right_max[i]) - walls[i])

    return total_water


# Test cases
if __name__ == "__main__":
    walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls1))  # Output: 6

    walls2 = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls2))  # Output: 6
