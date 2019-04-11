
class Graph:
    def __init__(self):

        self.graph={}
    
    def addEdge(self,v1,v2):
        if( v1 in self.graph):
            self.graph[v1].append(v2)
        else:
            self.graph[v1]=[v2]

    def bfs(self,v):
        visited=set()
        frontier=[v]#queue
        visited.add(v)

        while frontier:
            print(frontier)
            node=frontier.pop(0)
            print(node)
            for neighbour in self.graph[node]:
                if(neighbour not in visited):
                    visited.add(neighbour)
                    frontier.append(neighbour)        
    
    def bfs2(self,s):
        level={s:0}
        i=1
        frontier=[s]
        print(s)

        
        while frontier:
            next=[]
            for u in frontier :
                for v in self.graph[u]:
                    if v not in level:
                        print(v)
                        level[v]=i
                        next.append(v)
            frontier=next
            i+=1




m_graph= Graph()
m_graph.addEdge(0,1)
m_graph.addEdge(0,2)
m_graph.addEdge(1, 2) 
m_graph.addEdge(2, 0) 
m_graph.addEdge(2, 3) 
m_graph.addEdge(3, 3) 
m_graph.bfs(2)



