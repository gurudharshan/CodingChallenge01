# 1. Write a program to print the following
# 	Input: a2b6c3
# 	Output: aabbbbbbccc

a=input()
c=0
prev=a[0]

for i in range(0,len(a)):
    if prev!=a[i]:
        if a[i].isnumeric():
            c=(c*10)+int(a[i])
        else:
            print(prev*c,end="")
            c=0
            prev=a[i]
            
    
print(prev*c,end="")