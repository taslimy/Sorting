# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x




        # TO-DO: swap
        swapit = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = swapit




    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for x in range(len(arr)-1, 0, -1):
        for n in range(x):

            if arr[n] > arr [n + 1]:
                swap = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = swap
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr