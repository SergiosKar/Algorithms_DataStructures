

def edit_distance(str1,str2):

    n1=len(str1)
    n2= len(str2)
    dist=[ [ 0 for j in range(n2+1)] for i in range(n1+1)]

    for i in range(n1+1):
        for j in range(n2+1):

            if(i==0):
                dist[i][j]=j
            elif(j==0):
                dist[i][j]=i
            elif(str1[i-1]!=str2[j-1]):
                dist[i][j]=1+min(dist[i-1][j],dist[i-1][j-1],dist[i][j-1])
            else:
                dist[i][j]=dist[i-1][j-1]


    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in dist]))



str1='elephant'
str2='relevant'

edit_distance(str1,str2)

