m_array=[11,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]

def partition(array,low,high):

    pivot =array[high]
    i=low-1
    j=low

    while(j<high):
        if(array[j]<=pivot):
            i+=1
            array[i],array[j]=array[j],array[i]
        j+=1
    array[i+1],array[high]=array[high],array[i+1]  

    return(i+1)  

def quicksort(array,low,high):

    if(low<high):
        part_index=partition(array,low,high)

        quicksort(array,low,part_index-1)
        quicksort(array,part_index+1,high)

quicksort(m_array,0,len(m_array)-1)
m_array




