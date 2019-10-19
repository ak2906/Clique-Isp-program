# Clique-Isp-program
   Python Program for Clique Decision Problem and Independent Set Problem
##  Clique Decision Problem:
    A complete subgraph of a graph G=(V,E) is a clique.
    In this program(clique.py) we first take a matrix as the input, and ask the number of vertices.
    So the graph would have 4 vertices namely (0,1,2,3).
    The matrix with the size of the clique is passed to clique function.
    In clique function:
       In this function first we take the vertices for which we have to check if a clique exists or not.
       After this we check if there is no edge between 2 given vertices and also if they both belong to the clique set.
       If this condition satifies then failure occurs else success.
###       Input
    matrix=[[0,1,1,0],
            [1,0,1,1],
            [1,1,0,1],
            [0,1,1,0]]
            
###        Output
            Clique Set=[0,1,2]
            Clique is present [0,1,2]
            
###        Output
            Clique set=[0,1,3]
             No clique Present
###        Applications
             Clique-finding algorithms have been used in chemistry,to find chemicals that match a target structure and to model
             molecular docking  and the binding sites of chemical reactions.
## Independent Set Problem
   
    In independent set problem we check if 2 sets of vertices every vertex of one set is connected with all the vertices of another set
    and that no vertex of same set are connected to each other.
    
    In isp.py
     The function isp first gets set 1 of vertices and pushes remaining vertices in set2.
     It then checks if vertices of set 1 are connected to each other. if yes then failure occurs.
     Else it checks if vertices of set 2 are connected to each other. if yes then failure occurs.
     Then it checks if each vertex of set 1 are connected to all vertices of set 2.if no then failure occurs.
     After all these conditions are successfully checked then success occurs.
###     Input
       matrix=[[0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [1,1,1,0,0,0],
       [1,1,1,0,0,0],
       [1,1,1,0,0,0]]
       
###       Output 
          isp set=[0,1,2]
          Independent set present  [0,1,2]
      
###        Output
            isp set=[0,1,3]
            No Independent Set present
             
      
      
