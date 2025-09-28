"""
Kadane's Algorithm is an efficient method to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
It works by iterating through the array, keeping track of the current subarray sum and updating the maximum sum found so far.
This algorithm runs in O(n) time & O(1) space and is widely used for solving problems related to subarrays and dynamic programming.

Task:
Solve the LeetCode problem "Maximum Subarray" (LeetCode #53) using Kadane's Algorithm.

Example:
For array [−2,1,−3,4,−1,2,1,−5,4], Kadane's Algorithm finds the subarray 
[4,−1,2,1] with sum 6.

Algorithm:

1. Initialize two variables:
- max_current: The maximum sum of a subarray ending at the current position.
- max_global: The overall maximum sum found so far.

2. Iterate through the array:

- For each element, update max_current as the maximum of the current element and the sum of max_current plus the current element.
- Update max_global if max_current is greater than max_global.

3. Result:
- At the end, max_global holds the largest sum of any contiguous subarray.

"""

class Kadane():
    def maxSubArray(self,nums):
        # Initialize current and global maximum sums
        curSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            # Update max_current to be either the current or the sum with previous max_current
            curSum = max(nums[i],curSum + nums[i])
            # Update max_global if we found a new maximum
            maxSum = max(curSum,maxSum)
        return maxSum
        
# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Kadane().maxSubArray(nums))  # Output: 6