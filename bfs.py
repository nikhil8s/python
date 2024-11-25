graph={'A':['B','D','E','F'], 'D':['A'],'B': ['A', 'F','C' ],'F': ['B','A'], 'C': ['B'],'E': ['A']}

print("Given graph is:")waw

print(graph)

def dfs_traversal(input_graph,source):
    stack=list()
    visited_list=list()
    stack.append(source)
    visited_list.append(source)

while stack:

vertex=stack.pop()

print(vertex,end=" ")

for i in input_graph[vertex]:

if i not in visited_list:

stack.append(i)

visited_list.append(i)

print("DFS TRAVERSAL IS:")

dfs_traversal(graph,"A")