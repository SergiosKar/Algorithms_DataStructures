

A=[5,5,5,5,5,5,5]

def dotProduct(A):
    if len(A)==0:
        return 0
    elif len(A)==1:
        return A[0]
    else:
        return A[0]+dotProduct(A[1:])

dotProduct(A)