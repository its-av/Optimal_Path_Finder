import partition
import heapq
import wtdij
from collections import defaultdict
from decimal import Decimal
mygraph={}
graph={}
lines=[]
distances=[]
my_distance=[]
parentn={}

def update_graph(mycount,myid):
    a=mycount
    k=0
    se=0
    for i in range(a):
        fname=""
        if(i==0):
            fname=str(myid[0])+','+str(myid[1])+".txt"
            k+=1
        else:
            fname=str(myid[0])+','+str(myid[1])+'_'+str(k)+".txt"
            k+=1
        c_file = open(fname, "r")
        
        for line in c_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            if(line_list[0]=='##'):
                se=1
                continue
            elif(line_list[0]=='**'):
                se=-1
                continue
            elif(line_list[0]=='%%'):
                se=1
                continue
            if(se==1 and line_list[0]!='??' and line_list[0]!='##' and line_list[0]!='**' and line_list[0]!='%%' and line_list[0]!='Contents'):
                temp=line_list
                if(int(temp[0]) in graph.keys()):
                    graph[int(temp[0])][int(temp[1])]=Decimal(temp[2])
                else:
                    graph[int(temp[0])]={}
                    graph[int(temp[0])][int(temp[1])]=Decimal(temp[2])
            else:
                continue
        c_file.close()

def pathc(s,v):
    pathss=[]
    ftp=0
    while (v != s):
        pathss.append(v)
        if(v not in parentn.keys()):
            ftp=-1
            break
        else:
            v=parentn[v]
    pathss.append(s)
    pathss.reverse()
    if(ftp==-1):
        print("Path not exists")
    else:
        print("Length of the shortest path = ",len(pathss)-1)
        print(pathss)
        
def make_data():
    aaa=defaultdict(list)
    c_file = open("edges.txt", "r")
    for line in c_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        tp=(line_list[0],line_list[1])
        aaa[tp].append(line_list[2])
    tmp=aaa.keys()
    for j in tmp:
        xx=aaa[j]
        jj=list(j)
        lines.append([jj[0],jj[1],max(xx)])
    c_file.close()
make_data()
for i in range(len(lines)):
    temp=lines[i]
    if(int(temp[0]) in mygraph.keys()):
        mygraph[int(temp[0])][int(temp[1])]=Decimal(temp[2])
    else:
        mygraph[int(temp[0])]={}
        mygraph[int(temp[0])][int(temp[1])]=Decimal(temp[2])
total_nodes=len(partition.x)-1
def normalpath():
    print("Enter Source")
    source=int(input())
    if(source>total_nodes):
        print("Invalid Node")
        return
    print("Enter destination")
    dest=int(input())
    if(dest>total_nodes):
        print("Invalid Node")
        return
    global mygraph
    tempkey=mygraph.keys()
    for j in range(len(partition.x)):
        if j not in tempkey:
            mygraph[j]={}
    my_distance=wtdij.calculate_distances(mygraph, source)

    print("Weight of the shortest path = ",my_distance[dest])
    wtdij.pathc(source,dest)

def gridnormal():
    carry={}
    overblock,mainblock=0,0
    print("Enter Source")
    source=int(input())
    if(source>total_nodes):
        print("Invalid Node")
        return
    print("Enter destination")
    dest=int(input())
    if(dest>total_nodes):
        print("Invalid Node")
        return
    global graph
    tempkey=graph.keys()
    for j in range(len(partition.x)):
        if j not in tempkey:
            graph[j]={}
    distances = {vertex: float('infinity') for vertex in mygraph}
    distances[source] = 0
    pq = [(0, source)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        myid=partition.getc(partition.x[current_vertex],partition.y[current_vertex],partition.x_min,partition.y_min)
        mycount=partition.counter[myid[0]][myid[1]][1]+1
        temp=tuple(myid)
        if(temp not in carry.keys()):
            carry[temp]=1
            mainblock+=1
            overblock+=(mycount-1)
            update_graph(mycount,myid)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                parentn[neighbor]=current_vertex
        if(current_vertex==dest):
            break
    print("Weight of the shortest path = ",distances[dest])
    print("Total blocks loaded in memory = ",mainblock+overblock)
    print("Number of main blocks loaded = ",mainblock)
    print("Number of overflow blocks loaded = ",overblock)
    pathc(source,dest)
flag=0
while(flag!=-1):
    print("1: Normal Dijkstra\n2: Grid Dijkestra\nEnter -1 to exit")
    flag=int(input())
    if(flag==1):
        normalpath()
    elif(flag==2):
        gridnormal()
    else:
        continue
