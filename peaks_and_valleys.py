
Array=[1,2,3,5,6,3,5,2,3,5,3,2,3,2,2,1,3,7]          

def peaks_and_valleys(A):
    smaller=False
    for i in range(1,len(A)):
        if A[i-1]<A[i]:
            if(smaller):
                A[i-1],A[i]=A[i],A[i-1]
            
        else:
            if(not smaller):
                A[i-1],A[i]=A[i],A[i-1]

        smaller=not smaller

    return A

peaks_and_valleys(Array)