"""
Two Sum Problem (Leetcode #1):
This module provides two methods to solve the classic Two Sum problem:
Given an array of integers and a target value, find the indices of two numbers such that they add up to the target.
Methods:
1. twoSum (Hashing):
    - Uses a hash map to store previously seen numbers and their indices.
    - For each number, checks if its complement (target - current number) exists in the hash map.
    - Returns indices of the two numbers if found.
    - Time Complexity: O(n), where n is the number of elements in the array.
    - Space Complexity: O(n), due to the hash map storing up to n elements.
2. two_pointer (Sorting + Two Pointers):
    - Sorts the array while keeping track of original indices.
    - Uses two pointers (start and end) to find the pair that sums to the target.
    - Returns original indices of the two numbers if found.
    - Time Complexity: O(n log n), due to sorting.
    - Space Complexity: O(n), for storing pairs of numbers and indices.
Both methods return None if no valid pair is found.

"""

class TwoSum:
    def hashing(self, nums, target):
        seen = {}  # Stores number -> index
        for i in range(len(nums)):
            complement = target - nums[i]  # What number do we need to reach target?
            if complement in seen:
                # Found the pair
                return [seen[complement], i]
            seen[nums[i]] = i  # Store index of current number
        return None  # No solution found
    
    def two_pointer(self, nums, target):
        # Pair each number with its original index for tracking after sorting
        nums_with_indices = sorted((num, idx) for idx, num in enumerate(nums))
        i, j = 0, len(nums_with_indices) - 1  # Initialize two pointers
        while i < j:
            total = nums_with_indices[i][0] + nums_with_indices[j][0]  # Sum of values at pointers
            if total == target:
                # Found the pair, return their original indices
                return [nums_with_indices[i][1], nums_with_indices[j][1]]
            elif total < target:
                # If sum is less than target, move left pointer to increase sum
                i += 1
            else:
                # If sum is greater than target, move right pointer to decrease sum
                j -= 1
        return None  # No valid pair found

# Example usage of hashing method
arr = [2, 7, 11, 5]
print(TwoSum().twoSum(arr, 9))  # Output: [0, 1]


arr = [3, 0, 2, -2, -1, 4]
print(TwoSum().two_pointer(arr, 6))  # Output: [2, 5]

"""
Notes on Time and Space Complexity for Two Sum Problem:

- Hashing Method (twoSum):
    Time Complexity: O(n)      # Best for large arrays, single pass with hash map lookups.
    Space Complexity: O(n)     # Stores up to n elements in the hash map.

- Sorting + Two Pointers Method (two_pointer):
    Time Complexity: O(n log n) # Due to sorting step, slower than hashing for large n.
    Space Complexity: O(n)      # Stores pairs of numbers and their original indices.

Recommendation:
Use the hashing method for optimal performance unless array is already sorted or constraints require otherwise.
"""
# ...existing code...