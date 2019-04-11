array=[7,2,1,2,5,6,7,2,5,4,1,5,7]
base=[2,1,7,5]

for i in range(1,len(array)):

    base_index=-1
    for j in range(len(base)):
        if base[j]==array[i]:
            base_index=j
            break
    if( base_index==-1):
        continue
    else:
        if( base_index==0):
            stop=base[0]
        else:
           stop=base[base_index-1]
        k=i
        while(array[k-1]!=stop and k>0):
            array[k],array[k-1]=array[k-1],array[k]
            k-=1
           
array

