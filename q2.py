# 2. Write a program to print the inverse of the previous program
# 	Input: aabbbbbbccc
# 	Output: a2b6c3

n=input()
ans=""
temp=n[0]
c=0
for i in n:
    if temp==i:
        c=c+1
    else:
        ans=ans+temp+str(c)
        temp=i
        c=1
ans=ans+temp+str(c)
print(ans)
        
    
    
    