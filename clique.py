import random
import sys

def failure():
    print("No clique present")
    sys.exit()
def success(s):
    print("Clique present:")
    print(s)
def select(vertex):
    return random.choice(vertex)
def clique(m,v,t1,n):
    s=[]
    for i in range(t1):
    #         x=input(select(v))
        x=int(input("Select a vertex"))
        s.append(x)
    for i in range(n):
        x=bool(i in s)
        for j in range(n):
            if(i!=j):
                y=bool(j in s)
                if(m[i][j]==0 and x and y):
                    failure()  
    success(s)
    
n=int(input("Enter the no of vertex"))
matrix=[[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]
# matrix=[]
vertex1=[]
# print("Enter the entries rowwise:") 
# for i in range(n):
#     vertex1.append(i)
#     a =[] 
#     for j in range(n): 
#          a.append(int(input())) 
#     matrix.append(a) 
# For printing the matrix 
for i in range(n): 
    for j in range(n): 
        print(matrix[i][j], end = " ") 
    print() 
t=int(input("Enter the size of clique"))

clique(matrix,vertex1,t,n)