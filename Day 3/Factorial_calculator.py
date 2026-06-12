#Iterative Approach
num = int(input("Enter a number :"))
fact = 1
for i in range(1,num+1):
    fact*=i
print("Factorial =",fact)               
#Recursive Approach
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    num = int(input("enter a number:"))
    print("Factorial =",factorial))
