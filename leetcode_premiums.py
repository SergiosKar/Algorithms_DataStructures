# 683 k empty slots

# [1 3 5 7 2 4 6] flower that bloom on day[i]
# [1 5 2 6 3 7 4 ] day that flower[i] bloom
# using a sliding window of size 2 find if the middle is higher than all other in the window

days = [0] * len(flowers)
for day, position in enumerate(flowers, 1):
    days[position - 1] = day #[1 ]
ans = float('inf')
left, right = 0, k+1
while right < len(days):
    for i in range(left + 1, right):
        if days[i] < days[left] or days[i] < days[right]:
            left, right = i, i+k+1
            break
    else:
        ans = min(ans, max(days[left], days[right]))
        left, right = right, right+k+1

print(ans if ans < float('inf') else -1)

# 681. Next Closest Time

def nextClosestTime(time):
    digits = [int(digit) for digit in time if digit.isdigit()]
    uniques = sorted(set(digits))
    pos = [uniques.index(digit) for digit in digits]

    for i in range(3, -1, -1):
        pos[i] += 1
        if pos[i] < len(uniques):
            digits[i] = uniques[pos[i]]
            if digits[2] < 6 and digits[0]*10+digits[1] < 24:
                return "{}{}:{}{}".format(*digits)
        digits[i] = uniques[0]
    return "{}{}:{}{}".format(*digits)

print(nextClosestTime("19:39")) 

# 253 Meeting rooms 2
def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        SI = sorted(intervals, key=lambda it: (it.start, it.end))  # sorted intervals

        ret = 0
        heap = []  # contains end times

        for it in SI:
            start, end = it.start, it.end

            while heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

            ret = max(ret, len(heap))

        return ret


# 277 find the celebrity

# If One knows somebody else, then he cannot be a celebrity.
# If somebody doesn’t know A, then A cannot be a celebrity.

def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(candidate, i):  # All candidates < i are not celebrity candidates.
                candidate = i
        # Verify the candidate.
        for i in range(n):
            if i != candidate and (knows(candidate, i) \
                or not knows(i, candidate)):
                return -1
        return candidate



# 364 Nested List Weight Sum II 

# 1) convert to string and use a stack
# 2) Bfs


#298 Binary Tree Longest Consecutive Sequence


def btlcs(root):
    maxLength=0
    btlcs_helper(root)
    return maxLength
#top down
def btlcs_helper(root,parent,length):

    if not root:
        return length
    
    if parent and parent.val+1==root.val:
        length+=1
    else:
        length=1

    maxLength=max(length,maxLength)

    btlcs_helper(root.left,root,length)
    btlcs_helper(root.right,root,length)


# 418. Sentence Screen Fitting

def wordsTyping( sentence,  rows, cols) :
        string=''   
        for  s in sentence :
            s = s + " "
            string+=s
        
        start = 0
        for i in range(rows) :
            #place greedily
            start = start + cols
            #if last char of row is space--> well done move to next row
            if string[start % len(str)] == ' ':
                start+=1
            #else keep removing until find a space
            else:
                while start > 0 and string[(start-1) % len(string)] != ' ' :
                    start-=1
     
        return(start / len(string))
    
#361 Bomb enemy

# 0 E 0 0
# E 0 W E
# 0 E 0 0

def bomb_enemy(grid):
    max_hits=0
    dp=[[-1*len(grid[0])] for i in range(len(grid))]
    for row in grid:
        for col in row:
            if grid[row][col]=='0':
                hits=dfs(row,col,0)
                max_hits=max(hits,max_hits)
    
    return max_hits

def dfs(row,col,hits):
    
    if row>=len(grid)  or row<0:
        return 0
    if col>=len(grid[0]) or col<0:
        return 0

    if dp[row][col]!=-1:
    
        if grid[row][col]=='W':
            return hits
        
        if grid[row][col]=='E':
            for neigh in [(1,0),(-1,0),(0,1),(0,-1)]:
                hits+=dfs(neigh[0],neigh[1],hits)
        
        dp[row][col]=hits
    return dp[row][col]
        
    

#256 Paint house


# 1 2 1
# 2 1 3
# 1 2 4

# H H H
def paint_house(costs):

    if len(costs)==0:
        return 0

    
    for i in range(len(costs)):
        costs[i][0]=costs[i][0]+min(costs[i-1][1],costs[i-1][2])
        costs[i][1]=costs[i][1]+min(costs[i-1][0],costs[i-1][2])
        costs[i][2]=costs[i][2]+min(costs[i-1][0],costs[i-1][1])


    return min (costs[-1][0],costs[-1][1],costs[-1][2])


#276 Paint Fence

# Assuming there are 3 posts, if the first one and the second one has the same color, 
# then the third one has k-1 options. The first and second together has k options.
# If the first and the second do not have same color, 
# the total is k * (k-1), then the third one has k options. 
# Therefore, f(3) = (k-1)*k + k*(k-1)*k = (k-1)(k+k*k)

def paint_fence(n,k): # n posts, k colors
    
    ways=[0]*(n+1)
    ways[0]=k
    ways[1]=ways[0]*(k-1)+k
    for i in range(1,n+1):
        ways[i]=(ways[i-1]+ways[i-2])*(k-1)

    return ways[-1]

paint_fence(2,3)




















