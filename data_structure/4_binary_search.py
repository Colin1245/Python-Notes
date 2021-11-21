"""使用Python实现二分查找，并分析时间复杂度"""
#时间复杂度：O(logn)
def binary_search(lst, item):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == item:
            return True
        else:
            if item < lst[midpoint]:
                return binary_search(lst[:midpoint], item)
            else:
                return binary_search(lst[midpoint + 1:], item)

li = [45, 234, 34, 34, 9, 3465, 234, 1]
print("origin list:", li)
print("binary_search 3:",binary_search(li, 3))
print("binary_search 13:",binary_search(li, 13))