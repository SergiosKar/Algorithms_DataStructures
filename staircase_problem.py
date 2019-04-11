
#recursion
def count_ways(N):
    
    if N<=1 :
        return 1
    elif N==2:
        return 2
    else :
        return  count_ways(N-1) + count_ways(N-2)
   
count_ways(5)

#memoization
visited={}
def count_ways2(N):
    
    if (N in visited):
        return visited[N]
    else:   
        if N<=1 :
            return 1
        elif N==2:
            return 2
        else :
            ways=count_ways2(N-1) + count_ways2(N-2)
            visited[N]=ways
            return ways
   
count_ways2(5)


# dynamic programming(bottom up)
def count_ways3(N):
    ways=[]
    for i in range(N+1):
        if(i<=1):
            ways.append(1)
        elif i==2:
            ways.append(2)
        else:
            ways.append(ways[i-1]+ways[i-2])
        
    return ways[N]
   
count_ways3(5)



