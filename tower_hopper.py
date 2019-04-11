towers=[4,4,0,2,1,6]

#recursive
def min_jumps(towers,i,N):

    if i>=N:
        return 0
    
    if towers[i]==0:
        return float('Inf')
    
    min=float('Inf')
    for j in range(1,towers[i]+1):
        if(i+j)<=N:
            jumps=min_jumps(towers,i+j,N)
            if (jumps<min and jumps!=float('Inf')):
                min=1+jumps

    return min 
        
min_jumps(towers,0,6)


#dp
#jumps is minimum number of jumps to reach end
def min_jumps2(towers,N):

    jumps=[0 for i in range(N)]

    for i in range(N-1,-1,-1):
        
        if(towers[i]==0):
            jumps[i]=float('Inf')
        elif(towers[i]+i>N):
            jumps[i]=1
        else:
            min=float('Inf')
            for j in range(1,towers[i]+1):
                if(i+j<=N):
                    if( jumps[i+j] <min):
                        min=jumps[i+j]
            
            jumps[i] = min + 1
            
    print(jumps)
    return jumps[0]
        
min_jumps2(towers,6)



