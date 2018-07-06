# #冒泡排序
# list = [4, 8, 6, 9, 3, 7]
# print('原列表：', list)
#
# for i in range(len(list)):
#     for j in range(len(list)-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
# print('升序排序后的列表：', list)

def maopao():
    list = [3,5,2,7,8,1,6,9,4,0]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list
print(maopao())


def bubble_sort(blist):
    count = len(blist)
    for i in range(0, count):
        for j in range(i + 1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    return blist
blist = bubble_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
# print(blist)