import heapq
parent={}
pathss=[]
status={}
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    #distances[16]=float('infinity')
    print(distances)
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        status[current_vertex]=1
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            #print(neighbor)
            #print(neighbor)
            if(current_vertex==16):
                print()
            #print(distance[neighbor])
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                parent[neighbor]=current_vertex
    return distances

def pathc(s,v):
    pathss=[]
    ftp=0
    while (v != s):
        pathss.append(v)
        if(v not in parent.keys()):
            ftp=-1
            break
        else:
            v=parent[v]
    pathss.append(s)
    pathss.reverse()
    if(ftp==-1):
        print("Path not exists")
    else:
        print("Length of the shortest path = ",len(pathss)-1)
        print(pathss)
        



