# # 1)Description: Function to change list positive numbers into big
# # Input: list
# # Output: list with "big" inplace of any positive number
# arrayOfInt = [1, 2, 3, -1, -1]


# def returnBig(arrayOfInt):
#     for i in range(len(arrayOfInt)):
#         if arrayOfInt[i] < 0:
#             arrayOfInt[i] = "big"

#     return arrayOfInt


# print(returnBig(arrayOfInt))

# #2) Description: Function to
# # Input: list of numbers
# # Output

# listOfInt = [1, 2, 3, -4, 1, -2]


# def positive_value(listOfInt):
#     i = 0
#     numOfPositive = 0
#     while i < len(listOfInt):
#         if listOfInt[i] > 0:
#             numOfPositive += 1
#         i += 1

#     listOfInt[len(listOfInt) - 1] = numOfPositive

#     return listOfInt


# print(positive_value(listOfInt))

# # 3) description: function which takes a list and returns sum of list items
# #   input: list
# #   output: summation of input list

# listOfItems = [1, 1, 222, 1, 1]


# def sum_total(listOfItems):
#     k = 0
#     sumOfItems = 0
#     for k in listOfItems:
#         sumOfItems += k
#     return sumOfItems


# print(sum_total(listOfItems))

# # 4)desc: function will take a list and returns average
# #   input: list of number
# #   output: average

# listOfNums = [1, 2, 3, 4, 5]


# def average(lisfOfNums):
#     sumOfNums = 0
#     for i in listOfNums:
#         sumOfNums += i
#     return sumOfNums / len(lisfOfNums)


# print(average(listOfNums))

# # 5)desc: Create a function that takes a list and returns the length of the list.
# #   input: list of number
# #   output: length


# listOfItems = [1, 2, 3, 4, 5]


# def lengthOf(listOfItems):

#     return len(listOfItems)

# print(lengthOf(listOfItems))

# # 6)desc: Create a function that takes a list of numbers and returns the minimum
# #         value in the list. If the list is empty, have the function return False.
# #   input: list of number
# #   output: length

# listOfNum = [1, 2, 3, 2]


# def returnMin(list):
#     min = list[0]
#     for i in range(len(list)):
#         if len(list) == 0:
#             return False
#         elif list[i] < min:
#             min = list[i]
#     return min


# print(returnMin(listOfNum))

# # 7)desc: Create a function that takes a list of numbers and returns the max
# #         value in the list. If the list is empty, have the function return False.
# #   input: list of number
# #   output: length

# listOfNum = [1, 2, 3, 2]


# def returnMax(list):
#     max = list[0]
#     for i in range(len(list)):
#         if len(list) == 0:
#             return False
#         elif list[i] > max:
#             max = list[i]
#     return max


# print(returnMax(listOfNum))

# # 8)desc:  Create a function that takes a list and returns
# #            a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# #   input: list of number
# #   output: dict of max,min,len,avg,sum

# listOfItems = [1, 2, 3, 4, 5, 6, 7, 8]


# def ultimate_analysis(list):
#     myDict = {}
#     myDict["sumTotal"] = sum(list)
#     myDict["length"] = len(list)
#     myDict["max"] = max(list)
#     myDict["min"] = min(list)
#     myDict["average"] = sum(list) / len(list)

#     return myDict


# print(ultimate_analysis(listOfItems))

# 9)desc:  Reverse a list without using 2nd list
#   input: list
#   output: same list reversed


lst = ["ahmad", 2, 3, "alo", 5, 6, 7, 8, 9]


def reverse_list(list):
    #    solution(1) not working properly
    # temp = None
    # for i in range(len(list) / 2):
    #     temp = list[i]
    #     list[len(list) - 1 - i] = list[i]
    #     list[i] = temp

    #    solution(2) list = list[::-1] working using list slice (step size going backwards)
    #    solution(3) list.reverse()
    return list


print(reverse_list(lst))
