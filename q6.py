# 6. Find the number trailing zero's of the factorial of a number.
# 	Input: 5! = 120 Output: 1

n=int(input())
if n < 0:
    print(0)
elif n == 0 or n == 1:
    fact=0
else:
    fact = 1
    while(n > 1):
        fact *= n
        n -= 1
    
c=0
flag=True
while(flag):
    if fact==0:
        break
    else:
        if fact%10==0:
            c=c+1
            fact=fact//10
        else:
            flag=False
print(c)
            