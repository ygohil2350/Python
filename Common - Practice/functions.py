# Add Function
# def sum(a, b):
#     return a + b

# print(sum(2, 5))


# Remove duplicates
# def remove_duplicates(initial_list=[]):
#     final_list = []
#     for x in initial_list:
#         if x not in final_list:
#             final_list.append(x)
#     return final_list

# initial_list = [1, 2, 3, 4, 4, 5, 6, 77, 7, 7, 8, 9]
# print(remove_duplicates(initial_list))


# Maximum Count of Positive Integer and Negative Integer
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

# def maximumcount(nums):
#     positive = 0
#     negative = 0
#     for x in nums:
#         if x > 0:
#             positive += 1
#         elif x < 0:
#             negative += 1
#     return positive if positive > negative else negative


# nums = [-3, -2, -1, 0, 0, 1, 2]
# print(maximumcount(nums))


# Two Sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# def twoSum(nums: list[int], target: int):
#     position = []
#     for x in range(len(nums)):
#         for y in range(x + 1, len(nums)):
#             if nums[x] + nums[y] == target:
#                 position.append(x)
#                 position.append(y)
#                 return position


# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))


# Palindrome Number
# def isPalindrome(x: int):
#     return True if str(x) == str(x)[::-1] else False

# print(isPalindrome(121))
