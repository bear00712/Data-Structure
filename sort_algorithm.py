# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:05:19 2022

@author: user
"""
def bubble_sort(array):
    n = len(array)
    #每經過n次迭代會把第n大的排到第array[len(array) - n]個位置
    #只要執行n-1次
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def insertion_sort(array):    
    #從第2個元素開始比較
    #第n次迭代代表已經有n個數字排好了
    for i in range(1, len(array)):
        j = i
        while (j > 0) and (array[j-1] > array[j]) :
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array

def quick_sort(array):    
    # 找一個pivot，把arr分成左右兩邊，小的左邊大的右邊
    # 一直重複動作直到長度為1
    # 再把每個部份合起來
    if len(array) <= 1:
        return array
    else:        
        pivot = array.pop()        
        greater_list = []
        lower_list = []        
        for i in array:
            if i < pivot:
                lower_list.append(i)
            else:
                greater_list.append(i)        
    return quick_sort(lower_list) + [pivot] + quick_sort(greater_list)
    


def merge_sort(array):
    # 先把arr拆分到長度為1
    # 接著兩兩比較大小排好
    if len(array)<= 1:
        return array
    else:
        left_arr = array[:len(array)//2]
        right_arr = array[len(array)//2:]        
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0
    # 左右兩邊的arr遍例每個元素比較大小
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    # 左邊搜索完的話，把右邊還沒比到的全部加到result
    if left_idx == len(left):
        result += right[right_idx:]
    # 右邊搜索完的話，把左邊還沒比到的全部加到result
    if right_idx == len(right):
        result += left[left_idx:]
        
    return result  
        
        



a = [6,5,4,3,2,1,1,6]

   
bubble = bubble_sort(a.copy())
insert = insertion_sort(a.copy())
qucik = quick_sort(a.copy())
merge_ = merge_sort(a.copy())

