def binary_search(array,search_item,left=0,right=0):
    if right==0:
        left =0
        right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        
        if array[mid] == search_item:
            return mid
        elif array[mid]>search_item:
            right = mid-1
            return binary_search(array,search_item,left,right)
        elif array[mid]<search_item:
            left = mid +1
            return binary_search(array,search_item,left,right)
    return None


print(binary_search([1,2,3,4,5,6,7,8,9,10],5))