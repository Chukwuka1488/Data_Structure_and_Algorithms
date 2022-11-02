# Insert values into hash map
# def phone(obj):
#     # for i in range(N):
#     #     n = input()
#     #     if n in obj:
#     #         print(f"{n}={obj[n]}")
#     #     else:
#     #         print("Not found")
#     while True:
#         try:
#             k = input()
#             if k in obj.keys():
#                 print(f'{k}={cont[k]}')
#             else:
#                 print('Not found')
#         except EOFError:
#             break
#
#
# if __name__ == '__main__':
#     cont = dict(input().split() for _ in range(int(input())))
#     # for i in range(N):
#     #     d = input()
#     #     xd = d.split()
#     #     dd[xd[0]] = xd[1]
#     phone(cont)
import running_time

# people[name] = phone_number

# file1 = open('testcase_hash_dict.txt', 'r')
# Lines = file1.readlines()

# with open('testcase_hash_dict.txt') as f:
#     lines = [line.rstrip() for line in f]
#
# print(lines)
# # print(Lines)
cont = dict(input().split() for _ in range(int(input())))
running_time.time_to_run()
# print(cont)
while True:
    try:
        k = input()
        if k in cont.keys():
            print(f'{k}={cont[k]}')
        else:
            print('Not found')
    except EOFError:
        break
