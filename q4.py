# 4. Program to find the length of the longest word in the given input
# 	Input: welcome to sirius india team
# 	Output: welcome  7
n=input()
n=n.split(" ")
ans=n[0]
for i in n:
    if len(i)>len(ans):
        ans=i
print(len(ans))