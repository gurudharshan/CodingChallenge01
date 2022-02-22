# 5. Program to print the following pattern, Input will be number of rows
# 	             1

# 	            1 1

# 	           1 2 1

# 	          1 3 3 1

# 	         1 4 6 4 1

# 	     1 5 10 10 5 1

# 	  1 6 15 20 15 6 1

# 	1 7 21 35 35 21 7 1

n=int(input())
temp=[]
for i in range(1,n+1):
    arr=[]
    print((n-i)*" ",end="")
    for j in range(0,i):
        if i==1 or i==2:
            
            arr.append(1)
        else:
            if j==0:
                arr.append(1)
            elif j==i-1:
                arr.append(1)
            else:
                arr.append(temp[j-1]+temp[j])
    temp=arr
    for t in temp:
        print(t,end=" ")
    print()
            
            
        
