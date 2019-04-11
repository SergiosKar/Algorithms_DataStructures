
class Graph:
    def __init__(self):

        self.graph={}
    
    def addEdge(self,v1,v2):
        if( v1 in self.graph):
            self.graph[v1].append(v2)
        else:
            self.graph[v1]=[v2]

    def dfs(self,v):
        self.visited=[False for i in range(len(self.graph))]
        self.dfs_helper(v)

    def dfs_helper(self,v):

        self.visited[v]=True
        print(v)

        for i in self.graph[v]:
            if(self.visited[i]==False):
                self.dfs_helper(i)

    def dfs2(self,start):
        visited = []
        stack = [start]
        while stack != []:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                print(v)
            for w in (self.graph[v]):# reversed for tree if we want first left and then right
                if w not in visited:
                    stack.append(w)
        

    #dfs, push visited in stack,reverse stack
    def topological_sort(self):
        visited=[False for i in range(len(self.graph))]
        stack=[]

        for u in self.graph.keys():
            if visited[u] ==False :
                self.topological_sort_helper(u,visited,stack)

        stack.reverse()
        return stack

    def topological_sort_helper(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topological_sort_helper(i,visited,stack) 

        stack.append(v)





m_graph= Graph()
m_graph.addEdge(0,1)
m_graph.addEdge(0,2)
m_graph.addEdge(1, 2) 
m_graph.addEdge(2, 0) 
m_graph.addEdge(2, 3) 
m_graph.addEdge(3, 3) 
#m_graph.dfs(0)
m_graph.dfs2(0)
#m_graph.topological_sort()

# g = Graph() 
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3)
# g.topological_sort(0)





