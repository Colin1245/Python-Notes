"""使用Python实现选择排序，并分析时间复杂度"""
#时间复杂度：O（n**2）

def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

li = [45, 234, 34, 34, 9, 3465, 234, 1]
print("origin lst", li)
selection_sort(li)
print("selection_sort_list", li)