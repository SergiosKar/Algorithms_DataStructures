#945. Minimum Increment to Make Array Unique
def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        visited={}
        moves=0
        for i in range(len(A)):
            if(A[i] in visited):
                elem=A[i]
                while elem in visited:
                    elem+=1
                    moves+=1
                A[i]=elem
                visited[elem]=True
            else:
                visited[A[i]]=True
    
        return moves  

def minIncrementForUniqueOptimal(self, A):
        A.sort()
        A.append(100000)
        ans = taken = 0
        # find duplicates in sorted array ,store them
        # and then place as many of them as you can in range(A[i-1], A[i]) if A[i] is not duplicate
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) / 2 + give * A[i-1]
                taken -= give

        return int(ans)

#817. Linked List Components
def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G=set(G)
        i=head
        count=0
        while i is not None:
            if (i.val in G and getattr(i.next, 'val', None) not in G):
                count+=1
            
            i=i.next
        
        return count



# 9. Palindrome Number
def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        

        while x!=0:
            r=x%10

            count=0
            num=x
            while num>=10:
                num=num//10
                count+=1

            l=num
            x=x%(10**count)//10
        
            print(l,r,x)     
        
def isPalindrome2(n): 
  
    # Find the appropriate divisor 
    # to extract the leading digit 
    divisor = 1
    while (n / divisor >= 10): 
        divisor *= 10
  
    while (n != 0): 
          
        leading = n // divisor  
        trailing = n % 10
          
        # If first and last digit  
        # not same return false 
        if (leading != trailing):  
            return False
          
        # Removing the leading and  
        # trailing digit from number 
        n = (n % divisor)//10
          
        # Reducing divisor by a factor  
        # of 2 as 2 digits are dropped 
        divisor = divisor/100

        print(leading,trailing,n)
          
    return True



def isValid( s):
        """
        :type s: str
        :rtype: bool
        """
        
        def valid_parenth(st,el):
        
            prev=st[-1]
            
            if prev=='(' and el==')':
                return True
            elif prev=='[' and el==']':
                return True
            elif prev=='{' and el=='}':
                return True
            else:
                return False
            
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            
            print(s[i])
            print(stack)
            
            if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                stack.append(s[i])
            else:
                print(stack) 
                if(valid_parenth(stack,s[i])):
                    stack.pop()
                else:
                    return False

        if stack==[]:
            return True
        else:
            return False

isValid('()')




