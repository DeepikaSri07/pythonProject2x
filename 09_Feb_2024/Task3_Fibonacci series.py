# Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13

num = int(input("Enter the number of which want fibonacci series "))
n1,n2 = 0,1
n3=0
for i in range(0,num):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3
