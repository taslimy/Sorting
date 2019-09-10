# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    while len( arrA ) > 0 or len( arrB ):
      if not len(arrA):
        merged_arr.extend( arrB )
        arrB=[]

      if not len(arrB):
        merged_arr.extend( arrA )
        arrA=[]
      else:
          if arrA[0] < arrB[0]:
             merged_arr.append(arrA[0])
             arrA.pop(0)
          else:
             merged_arr.append(arrB[0])
             arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
      # if arr length is 1 return it
    if len(arr) <= 1:
        return arr
    # find the split point
    split = int(len(arr)/2) # << divide to split em has to be int for some reason it was floating.....
    # have a start index and and end index
    arrA = arr[:split]
    arrB = arr[split:]
    # We not need to put them in a left side and a right side and get a result
    left = merge_sort(arrA)
    right = merge_sort(arrB)
    # merge left and right
    res = merge(left, right)
    return res



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
