array=[4,6,8,13,3,5,10,1,2,7,8,3,5,8,9,1,3,23,2,12,4]


def linear_search(array,value):
    for el in array:
        if el==value:
            print( array.index(el))
            return el

linear_search(array,23)

def binary_search(array,value):
    first=0
    last=len(array)-1

    for i in range(0,len(array)-1):
        middle=round((last+first)/2)
        if(array[middle]==value):
            print('Found: '+str(middle))
            break
        else:
            if(value<array[middle]):
                last=middle-1
            elif(value>array[middle]):
                first=middle+1 

#does not return index
def binary_search2(array,value):

    if len(array)<1:
        print('Not found')
        return
    
    middle=len(array)//2
    if(array[middle]==value):
            print('Found')
    else:
        if(value<array[middle]):
            binary_search2(array[:middle-1],value)
        elif(value>array[middle]):
            binary_search2(array[middle+1:],value)



array2=[2,4,5,5,7,8,8,9,11]
binary_search(array2,11)
array2=[2,4,5,5,7,8,8,9,11]
binary_search2(array2,5)
