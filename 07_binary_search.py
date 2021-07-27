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
''''递归实现'''
def binary_search(alist,item):
    '''二分查找法'''
    n = len(alist)
    if n>0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

# '''测试'''
# if __name__ == "__main__":
#      li = [54,26,93,17,77,31,55,20]
#
#      print(binary_search(li, 55))
#      print(binary_search(li, 31))




# ''''非递归实现'''
# def binary_search(alist,item):
#      '''二分查找法'''
#      n = len(alist)
#      first = 0
#      last = n-1
#      while first <= last:
#          mid = (first+last)//2
#          if alist[mid] == item:
#                  return True
#          elif item < alist[mid]:
#              last = mid - 1
#          else:
#              first = mid + 1
#      return False

'''测试'''
if __name__ == "__main__":
     li = [54,26,93,17,77,31,55,20]
     sorted_li = merge_sort(li)
     # 天老爷呀！要查找的一定是有序表！！！
     print(binary_search(sorted_li, 55))
     print(binary_search(sorted_li, 31))