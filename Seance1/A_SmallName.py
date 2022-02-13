# nbMot = int(input())
#
# i = 0
# tmp = input()
# while i < nbMot - 1:
#     read = input()
#
#     len_read = len(read)
#     len_tmp = len(tmp)
#     if len_read < len_tmp:
#         tmp = read
#
#     if len_read == len_tmp:
#         if (read < tmp):
#             tmp = read
#     i += 1
#
# print(tmp)

print(min([input() for _ in range(int(input()))], key=lambda s: (len(s), s)))
