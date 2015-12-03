'''
Implement binary search.

Input:
    Find the index of 4 in [1, 4, 7, 8]
Output:
    1
'''

def binary_search(lst, lo, hi, target):
    if hi - lo ==0:
        return lo
    if hi - lo < 0:
        return flase
    mid = (hi + lo)//2
    if target < lst[mid]:
        return binary_search(lst, lo, mid-1, target)
    if target > lst[mid]:
        return binary_search(lst, mid+1, hi, target)
    return mid

print(binary_search([1, 4, 7, 8], 0, 3, 4))
print(binary_search([1, 4, 7, 8], 0, 3, 5))
