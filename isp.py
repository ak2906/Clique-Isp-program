import sys
def select(vertex):
    return random.choice(vertex)
def failure():
    print("No independent set present")
    sys.exit()
def success(s1,s2):
    print("Independent set present")
    print(s1)
    print(s2)
def isp(m,vertex1,t1,n):
    s1=[]
    s2=[]
    for i in range(t1):
        x=int(input("Select a vertex"))
        s1.append(x)
    for i in range(n):
        b=bool(i in s1)
        if(b==False):
            s2.append(i)
#     print(s2)
    for i in range(len(s1)):
        x=int(s1[i])
        for j in range(len(s1)):
            y=int(s1[j])
            if(m[x][y]==1):
                failure()
    for i in range(len(s2)):
        x=int(s2[i])
        for j in range(len(s2)):
            y=int(s2[j])
            if(m[x][y]==1):
                failure()
    for i in range(len(s1)):
        x=int(s1[i])
        for j in range(len(s2)):
            y=int(s2[j])
            if(m[x][y]==0):
                failure()
    success(s1,s2)
n=int(input("Enter the no of vertex"))
matrix=[[0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [1,1,1,0,0,0],
       [1,1,1,0,0,0],
       [1,1,1,0,0,0]]
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
t=int(input("Enter the size of Independent Set"))
isp(matrix,vertex1,t,n)