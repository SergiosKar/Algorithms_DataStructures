def insertion_sort(array):
    for i in range(1,len(array)):
        j=i
        while j>=0:
            if(array[j]<array[j-1]):
                array[j-1],array[j]=array[j],array[j-1]
                j-=1
            else:
                break


def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range(i,len(array)-1):
            if array[i]>array[j+1] :
                array[j+1],array[i]=array[i],array[j+1]

def merge_sort(arr):

    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Compare
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  

def shell_sort(array):
    # Start with a big gap, then reduce the gap 
    n = len(array) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = array[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and array[j-gap] >temp: 
                array[j] = array[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            array[j] = temp 
        gap=gap// 2

    

def selection_sort(array):
    index_of_sorted=0

    for i in range(0,len(array)):
        min=100
        for j in range(index_of_sorted,len(array)):
            if(array[j]<min):
                min=array[j]
                min_index=j

        array[i],array[min_index]=min,array[i]
        index_of_sorted+=1


def counting_sort(array):
    counts=[0 for i in range(max(array)+1)]
    for i in range(len(array)):
        counts[array[i]]+=1
    
    for i in range(1,len(counts)):
        counts[i]+=counts[i-1]
    result=[0 for i in range(len(array))]
    for i in range(len(array)):
        result[counts[array[i]]-1]=array[i]
        counts[array[i]]-=1

    for i in range(0,len(array)): 
        array[i] = result[i] 

def counting_sort_with_base(arr, exp1,b): 
  
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (b) 
  
    for i in range(0, n): 
        index = int(arr[i]/exp1) 
        count[ (index)%b ] += 1
  

    for i in range(1,b): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        index = int(arr[i]/exp1) 
        output[ count[ (index)%b ] - 1] = arr[i] 
        count[ (index)%b ] -= 1
        i -= 1
  
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
def radix_sort(arr): 
  
    max1 = max(arr) 
    base=10
    exp = 1
    while max1/exp > 0: 
        counting_sort_with_base(arr,exp,base) 
        exp *= base


m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
insertion_sort(m_array)
m_array
m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
bubble_sort(m_array)
m_array
m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
merge_sort(m_array)
m_array
m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
shell_sort(m_array)
m_array
m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
selection_sort(m_array)
m_array
m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
counting_sort(m_array)
m_array
m_array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]
radix_sort(m_array)
m_array





