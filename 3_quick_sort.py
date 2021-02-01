"""使用Python实现快速排序，并分析时间复杂度"""
#时间复杂度：O（n**2）
def quick_sort(lst, start, end):
    if start >= end:
        return

    mid = lst[start]
    low = start
    high = end

    while low < high:
        while low < high and lst[low] >= mid:
            high -= 1
        lst[low] = lst[high]

        while low < high and lst[low] < mid:
            low += 1
        lst[high] = lst[low]

    lst[low] = mid

    quick_sort(lst, start, low - 1)
    quick_sort(lst, low + 1, end)

li = [45, 234, 34, 34, 9, 3465, 234, 1]
print("origin:", li)
quick_sort(li, 0, len(li) - 1)
print("quick_sort:", li)

