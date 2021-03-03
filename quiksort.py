"""
快速排序算法
"""


def sort(arr, low, high):
    """
    快速排序，先找基准点进行分区，比基准点大的在基准点之后，比基准点小的在基准点之前，然后进行递归
    :param arr: 待排序的列表
    :param low: 开始位置
    :param high: 结束位置
    :return:
    """
    if low >= high:
        return
    pos = partition(arr, low, high)
    sort(arr, low, pos)
    sort(arr, pos + 1, high)


def partition(arr, low, high):
    base = arr[low]
    x = low
    y = high
    while x < y:
        while x < y and arr[y] >= base:
            y -= 1
        while x < y and arr[x] <= base:
            x += 1
        if x < y:
            t = arr[x]
            arr[x] = arr[y]
            arr[y] = t
            x += 1
            y += 1
    arr[low] = arr[x]
    arr[x] = base
    return y


arr = [56, 78, 4, 3, 90, 77, 100, 7, 67, 23, 56]
sort(arr, 0, len(arr) - 1)
print(arr)
