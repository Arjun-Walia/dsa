#Given a string A of size N, find and return the longest palindromic substring in A.

def longestPalindrome(A):
    if len(A) == 0:
            return ""
        
    res=""
    resLen=0
    
    for i in range(len(A)):
        
        l,r=i,i
        #odd len
        while l>=0 and r<len(A) and A[r]==A[l]:
            if r-l+1>resLen:
                resLen=r-l+1
                res=A[r:l+1]
                
            l-=1
            r+=1
            
        l,r=i+1,i
        #even len
        while l>=0 and r<len(A) and A[r]==A[l]:
            if r-l+1>resLen:
                resLen=r-l+1
                res=A[r:l+1]
                
            l-=1
            r+=1
            
    return res