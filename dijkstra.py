# ALGORITHM
# DEFAULTS TO -1 IF NO PATH IS FOUND

def dijkstra(n: int, edges: list[list[int]], src: int) -> dict:
    # PREPARING DICT FOR ANSWEAR
    mydict = {}
    for i in range(n):
        mydict[i] = -1
    mydict[src] = 0

    # SOME VARIABLES NEEDED FOR MY CODE TO WORK
    now = src
    last = mydict[now]
    nonecount = 0

    # THE MEAT
    while len(edges) and nonecount < 2:

        # CHOOSING NEXT EDGE TO WORK WITH
        i = 0
        while i < len(edges) and edges[i][0] != now:
            i += 1
        if i != len(edges):
            edge = edges.pop(i)
            nonecount = 0
        else:
            edge = None
            nonecount += 1

            # LOOKING FOR NEXT LOWEST VALUE EDGE 
            lowest = float('inf')
            for j in mydict:
                if mydict[j] > last and mydict[j] < lowest:
                    lowest = mydict[j]
                    now = j
        last = mydict[now]

        # CHECKING AND CHANGING PATH IF SHORTER IS FOUND
        if edge != None:
            if mydict[edge[1]] == -1:
                mydict[edge[1]] = mydict[now] + edge[2]
            elif mydict[edge[1]] > mydict[now] + edge[2]:
                mydict[edge[1]] = mydict[now] + edge[2]  

    return mydict


# EXAMPLES TO UNCOMMENT AND CHECK

# EDGES IN FORMAT [u, v, w] 
# u is the source vertex 
# v is the destination vertex
# w is the weight of the edge


# n=5
# edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]]
# src=0


# n=4
# edges=[[0,1,3],[1,2,8],[2,3,4],[3,0,2]]
# src=0

n=3
edges=[[0,1,4]]
src=0

# n=5
# edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]]
# src=4


print(dijkstra(n, edges, src))