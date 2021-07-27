# coding utf-8
def merge_sort(alist):
    ''''归并排序'''

    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    # 采用归并排序后新的有序的子列表
    left_l = merge_sort(alist[:mid]) # 传入的是新的列表（子序列）
    right_l = merge_sort(alist[mid:])

    # 将两个有序的子序列 合并成一个新的整体
    left_pointer = 0
    right_pointer = 0
    result = [] # 存放结果

    while left_pointer < len(left_l) and right_pointer < len(right_l):
        if left_l[left_pointer] < right_l[right_pointer]:
            result.append(left_l[left_pointer])
            left_pointer += 1
        else:
            result.append(right_l[right_pointer])
            right_pointer += 1

    # 合并排序后的结果
    result += left_l[left_pointer:]
    result += right_l[right_pointer:]

    return result

'''测试'''
if __name__ == "__main__":
    li = [54,26,93,17,77,31,55,20]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)