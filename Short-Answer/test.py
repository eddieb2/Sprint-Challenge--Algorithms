# >>> O(n)
# a = 0
# n = 4
# while (a < n * n * n):
#     a = a + n * n
#     print(a)

# as n increase > a increases linearly

# >>> O(n log n)
# sum = 0
# n = 10
# for i in range(n):
#   j = 1
#   while j < n:
#     j *= 2
#     sum += 1
# print(sum)
#            2x 3x 3x  3x  3x  4x  4x  4x
# n=   1, 2, 3, 4,  5,  6,  7,  8,  9, 10
# sum= 0, 2, 6, 8, 15, 18, 21, 24, 36, 40

# the number being returned is double the number of bunnies
# but the num of operations increases linearly
# def bunnyEars(bunnies):
#   if bunnies == 0:
#     return 0
#   print(bunnies)
#   return 2 + bunnyEars(bunnies - 1)
# bunnyEars(10)
# # print(bunnyEars(2))


# bunnies = 1, 2, 3, 4,  5,  6,  7,  8,  9, 10
#           2, 4, 6, 8, 10, 12, 14, 16, 18, 20