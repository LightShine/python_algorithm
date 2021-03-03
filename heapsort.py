"""
堆排序
"""


def swap(arr: list, a, b):
    """
    列表内数据交换
    :param arr: 列表
    :param a: 位置a
    :param b: 位置b
    :return:
    """
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t


def adjust_heap(arr: list, start, end):
    tmp = arr[start]
    pos = start
    i = start * 2 + 1
    while i < end:
        if i + 1 < end and arr[i] < arr[i + 1]:
            i += 1
        if arr[i] > tmp:
            arr[pos] = arr[i]
            pos = i
        else:
            break
        i = i * 2 + 1
    arr[pos] = tmp


def sort(arr: list):
    """
    堆排序，从第一个非叶子节点开始调整
    :param arr: 待排序列表
    :return:
    """
    for i in range(len(arr) // 2 - 1, -1, -1):
        adjust_heap(arr, i, len(arr))
    for j in range(len(arr) - 1, -1, -1):
        swap(arr, 0, j)
        adjust_heap(arr, 0, j)


arr = [56, 78, 4, 3, 90, 77, 100, 7, 67, 23, 56]
sort(arr)
print(arr)
