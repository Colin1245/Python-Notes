"""使用Python实现冒泡排序，并分析时间复杂度"""
#时间复杂度：O（n**2）

def bubble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i +1], lst[i]

li = [45, 234, 34, 34, 9, 3465, 234, 1]
bubble_sort(li)
print(li)