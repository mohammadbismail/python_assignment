# # # 1)Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one
# # # , from the number (as the 0th element) down to 0 (as the last element).

# num = 5
# arr = []


# def count_down(num):

#     for i in range(num, -1, -1):
#         arr.append(i)
#     return arr


# print(count_down(num))

# # # 2)Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second
# arr = [1, 6]


# def printerFun(arr):
#     print(arr[0])
#     return arr[1]


# print(printerFun(arr))

# # 3)Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

# arr = [4, 2, 4, 5, 6, 7]


# def sumOf(arr):
#     sum = arr[0] + len(arr)
#     print(arr[0])
#     return sum


# print(sumOf(arr))


# # # 4)Write a function that accepts a list and creates a new list containing only the values from the original list
# # #  that are greater than its 2nd value. Print how many values this is and then return the new list. If the list
# # #  has less than 2 elements, have the function return False

# arr = [4, 3, 7]
# newArr = []


# def greater2ndIndex(arr):
#     for i in range(len(arr)):
#         if len(arr) < 2:
#             return False
#         elif i == 1:
#             continue
#         elif arr[i] > arr[1]:
#             newArr.append(arr[i])
#     return newArr


# print(greater2ndIndex(arr), len(newArr))


# # This funcation will take a size of an array and value and returns an array with provided size with the given value
# # Input: two integers arraysize and arrayvalues
# # Output: array of given size and repeated given value
# # desc: ex if we give 4 and 7 it will return [7,7,7,7]
# outputArray = []
# arrayValue = 9
# arrayLength = 4


# def arrayOfDuplicates(arrayLength, arrayValue):
#     i = 0
#     while i < arrayLength:
#         outputArray.append(arrayValue)
#         i += 1
#     return outputArray


# print(arrayOfDuplicates(arrayLength, arrayValue))
