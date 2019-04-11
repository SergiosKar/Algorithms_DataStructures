class knapSack:

    def __init__(self,weights,values):
        self.weights=weights
        self.values=values
        self.cache={}


    #recursion
    def recurs_func(self, W , n):

        if(n==0 or W==0):
            return 0
        elif(self.weights[n-1]>W):
            return self.recurs_func(W,n-1)
        else:
            return max(self.recurs_func(W,n-1),self.values[n-1]+self.recurs_func(W-self.weights[n-1],n-1) )
        
    #dp with memoization
    def dp(self,W  , n):
        if((W,n) in self.cache):
            return self.cache[(W,n)]
        else:
                
            if(n==0 or W==0):
                return 0
            elif(self.weights[n-1]>W):
                c1=self.dp(W,n-1)
                self.cache[(W,n)]=c1
                return c1
            else:
                c1=self.dp(W,n-1)
                c2=self.dp(W-self.weights[n-1],n-1)
                c= max(c1,self.values[n-1]+c2 )
                self.cache[(W,n)]=c
                return c
            
    def bottomup(self,W,n):

        KS = [[0 for x in range(W+1)] for x in range(n+1)] 
  
   
        for i in range(n+1): 
            for w in range(W+1): 
                if i==0 or w==0: 
                    KS[i][w] = 0
                elif self.weights[i-1] <= w: 
                    KS[i][w] = max(self.values[i-1] + KS[i-1][w-self.weights[i-1]],  KS[i-1][w]) 
                else: 
                    KS[i][w] = KS[i-1][w] 

        return KS[n][W] 



values = [60, 100, 120] 
weights = [10, 20, 30] 
W=50
ks= knapSack( weights , values) 
#ks.recurs_func(W,len(weights))
#ks.dp(W,len(weights))
ks.bottomup(W,len(weights))


