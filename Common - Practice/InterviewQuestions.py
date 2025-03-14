# input = "aabbcdeee"
# output = "2a2b1c1d3e"


# def stringChecker(initialStr: str) -> str:
#     currentWord = ""
#     currentCount = 0
#     outputStr = ""
#     for x in initialStr:
#         if currentWord != x:
#             if currentCount > 0:
#                 outputStr += str(currentCount) + currentWord
#             currentWord = x
#             currentCount = 1
#         elif currentWord == x:
#             currentCount += 1
#     outputStr += str(currentCount) + currentWord
#     return outputStr


# print(stringChecker("aabbcdeee"))
