import math
from decimal import Decimal
from collections import defaultdict
grids=[]
counter=[]
print("Enter Grid Size: ")
k=int(input())
print("Enter Block Size: ")
bsize=int(input())


def create_grid(x_max,y_max,x_min,y_min):
  x=x_min
  y=y_min
  i=0
  while(x<=x_max):
    arr=[]
    ap=[]
    y=y_min
    j=0
    while(y<=y_max):
      grid=[x,y,x+k,y+k]
      vv=[0,0,0,0,0,0]
      arr.append(grid)
      ap.append(vv)
      y+=k
      j+=1
    if(arr):
      grids.append(arr)
      counter.append(ap)
    x+=k
    i+=1


def getc(x,y,xx,yy):
  rer=[]
  rer.append(int((x-xx)/k))
  rer.append(int((y-yy)/k))
  return rer

# write nodes
def write(cordnt,xx,yy,nono):
  fname=""
  tname=""
  if(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]==0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
  elif(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]>0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
  else:
    counter[cordnt[0]][cordnt[1]][0]=1
    counter[cordnt[0]][cordnt[1]][1]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
    if(counter[cordnt[0]][cordnt[1]][1]-1==0):
        tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
        r_file=open(tname,"a")
        r_file.write("?? "+fname)
        r_file.close()

        r_file=open(fname,"a")
        r_file.write("Contents of Overflow disk block")
        r_file.write("\n")
        r_file.write("?? "+tname)
        r_file.write("\n")
        r_file.close()

    elif(counter[cordnt[0]][cordnt[1]][1]>=2):
        sss=counter[cordnt[0]][cordnt[1]][1]-1
        tname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(sss)+".txt")
        r_file=open(tname,"a")
        r_file.write("?? "+fname)
        r_file.close()

        r_file=open(fname,"a")
        r_file.write("Contents of Overflow disk block")
        r_file.write("\n")
        tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
        r_file.write("?? "+tname)
        r_file.write("\n")
        r_file.close()

  b_file=open(fname,"a")
  b_file.write(str(nono)+" "+str(xx)+" "+str(yy))
  b_file.write("\n")
  
# write edges within cell
def write2(cordnt,xx,yy,wt):
  fname=""
  tname=""
  if(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]==0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
  elif(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]>0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
  else:
    counter[cordnt[0]][cordnt[1]][0]=1
    counter[cordnt[0]][cordnt[1]][1]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
    if(counter[cordnt[0]][cordnt[1]][1]-1==0):
      tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
      r_file=open(tname,"a")
      r_file.write("?? "+fname)
      r_file.close()

      r_file=open(fname,"a")
      r_file.write("Contents of Overflow disk block")
      r_file.write("\n")
      r_file.write("?? "+tname)
      r_file.write("\n")
      r_file.close()

    elif(counter[cordnt[0]][cordnt[1]][1]>=2):
      tname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1]-1)+".txt")
      r_file=open(tname,"a")
      r_file.write("?? "+fname)
      r_file.close()

      r_file=open(fname,"a")
      r_file.write("Contents of Overflow disk block")
      r_file.write("\n")
      tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
      r_file.write("?? "+tname)
      r_file.write("\n")
      r_file.close()

  b_file=open(fname,"a")
  if(counter[cordnt[0]][cordnt[1]][2]==0):
    counter[cordnt[0]][cordnt[1]][2]=1
    b_file.write("##")
    b_file.write("\n")
  b_file.write(str(xx)+" "+str(yy)+" "+str(wt))
  b_file.write("\n")

# write boundary nodes
def write3(cordnt,xx,yy,jjh):
  fname=""
  tname=""
  if(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]==0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
  elif(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]>0 ):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
  else:
    counter[cordnt[0]][cordnt[1]][0]=1
    counter[cordnt[0]][cordnt[1]][1]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
    if(counter[cordnt[0]][cordnt[1]][1]-1==0):
      tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
      r_file=open(tname,"a")
      r_file.write("?? "+fname)
      r_file.close()

      r_file=open(fname,"a")
      r_file.write("Contents of Overflow disk block")
      r_file.write("\n")
      r_file.write("?? "+tname)
      r_file.write("\n")
      r_file.close()

    elif(counter[cordnt[0]][cordnt[1]][1]>=2):
      tname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1]-1)+".txt")
      r_file=open(tname,"a")
      r_file.write("?? "+fname)
      r_file.close()

      r_file=open(fname,"a")
      r_file.write("Contents of Overflow disk block")
      r_file.write("\n")
      tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
      r_file.write("?? "+tname)
      r_file.write("\n")
      r_file.close()

  b_file=open(fname,"a")
  if(counter[cordnt[0]][cordnt[1]][2]==0):
    counter[cordnt[0]][cordnt[1]][2]=1
    b_file.write("##")
    b_file.write("\n")
  if(counter[cordnt[0]][cordnt[1]][3]==0):
    counter[cordnt[0]][cordnt[1]][3]=1
    b_file.write("**")
    b_file.write("\n")
  b_file.write(str(jjh)+" "+str(xx)+" "+str(yy))
  b_file.write("\n")
  b_file.close()
    
# write boundary edges
def write4(cordnt,xx,yy,wtt):
  fname=""
  tname=""
  if(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]==0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
  elif(counter[cordnt[0]][cordnt[1]][0]<bsize and counter[cordnt[0]][cordnt[1]][1]>0):
    counter[cordnt[0]][cordnt[1]][0]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
  else:
    counter[cordnt[0]][cordnt[1]][0]=1
    counter[cordnt[0]][cordnt[1]][1]+=1
    fname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1])+".txt")
    if(counter[cordnt[0]][cordnt[1]][1]-1==0):
      tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
      r_file=open(tname,"a")
      r_file.write("?? "+fname)
      r_file.close()

      r_file=open(fname,"a")
      r_file.write("Contents of Overflow disk block")
      r_file.write("\n")
      r_file.write("?? "+tname)
      r_file.write("\n")
      r_file.close()

    elif(counter[cordnt[0]][cordnt[1]][1]>=2):
      tname=str(str(cordnt[0])+","+str(cordnt[1])+"_"+str(counter[cordnt[0]][cordnt[1]][1]-1)+".txt")
      r_file=open(tname,"a")
      r_file.write("?? "+fname)
      r_file.close()

      r_file=open(fname,"a")
      r_file.write("Contents of Overflow disk block")
      r_file.write("\n")
      tname=str(str(cordnt[0])+","+str(cordnt[1])+".txt")
      r_file.write("?? "+tname)
      r_file.write("\n")
      r_file.close()
      
  b_file=open(fname,"a")
  if(counter[cordnt[0]][cordnt[1]][3]==0):
    counter[cordnt[0]][cordnt[1]][3]=1
    b_file.write("**")
    b_file.write("\n")
  if(counter[cordnt[0]][cordnt[1]][4]==0):
    counter[cordnt[0]][cordnt[1]][4]=1
    b_file.write("%%")
    b_file.write("\n")
  b_file.write(str(xx)+" "+str(yy)+" "+str(wtt))
  b_file.write("\n")


def display(fname):
  print()
  myfile=open(fname,"r")
  for line in myfile:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    print(*line_list, sep=" ")
  print()


def visualiser(targetid):
  if(counter[targetid[0]][targetid[1]][0]==0):
    print("Does not exist")
  else:
    fname=str(str(targetid[0])+","+str(targetid[1])+".txt")
    if(counter[targetid[0]][targetid[1]][1]==0):
      display(fname)
    else:
      display(fname)
      temp=1
      for k in range(counter[targetid[0]][targetid[1]][1]):
        fname=str(str(targetid[0])+","+str(targetid[1])+"_"+str(temp)+".txt")
        temp+=1
        display(fname)


a_file = open("nodes.txt", "r")
list_of_lists = []
x=[]
y=[]
maxnn=0
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  x.append(Decimal(line_list[1]))
  y.append(Decimal(line_list[2]))
  list_of_lists.append(line_list)
a_file.close()
maxnn=len(x)
x_max=max(x)
y_max=max(y)
x_min=min(x)
y_min=min(y)
x_max+=math.ceil(x_max-x_min)%k
y_max+=math.ceil(y_max-y_min)%k
create_grid(x_max,y_max,x_min,y_min)
all_ids=[]
for i in range(len(x)):
  xx=x[i]
  yy=y[i]
  myc=getc(xx,yy,x_min,y_min)
  all_ids.append(tuple(myc))
  write(myc,xx,yy,i)
aaa=defaultdict(list)
lines=[]
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
for line in lines:
  line_list = line
  ii=int(line_list[0])
  jj=int(line_list[1])
  weight=Decimal(line_list[2])
  stor1=getc(x[ii],y[ii],x_min,y_min)
  stor2=getc(x[jj],y[jj],x_min,y_min)
  all_ids.append(tuple(stor1))
  all_ids.append(tuple(stor2))
  if(stor1==stor2):
    write2(stor1,ii,jj,weight)
graph = defaultdict(list)
for line in lines:
  line_list = line
  ii=int(line_list[0])
  jj=int(line_list[1])
  stor1=getc(x[ii],y[ii],x_min,y_min)
  stor2=getc(x[jj],y[jj],x_min,y_min)
  all_ids.append(tuple(stor1))
  all_ids.append(tuple(stor2))
  if(stor1!=stor2):
    graph[tuple(stor1)].append(jj)
    graph[tuple(stor2)].append(ii)
key=graph.keys()
key=list(key)
for i in key:
  ss=i
  ele=set(graph[i])
  ele=list(ele)
  ele=sorted(ele)
  for j in range(len(ele)):
    write3(ss,x[ele[j]],y[ele[j]],ele[j])
for line in lines:
  line_list = line
  ii=int(line_list[0])
  jj=int(line_list[1])
  weight=Decimal(line_list[2])
  stor1=getc(x[ii],y[ii],x_min,y_min)
  stor2=getc(x[jj],y[jj],x_min,y_min)
  all_ids.append(tuple(stor1))
  all_ids.append(tuple(stor2))
  if(stor1!=stor2):
    write4(stor1,ii,jj,weight)
    write4(stor2,ii,jj,weight)
all_ids=set(all_ids)
all_ids=list(all_ids)
fname=""
for j in range(len(all_ids)):
  ss=all_ids[j]
  if(counter[ss[0]][ss[1]][2]==0):
    counter[ss[0]][ss[1]][2]=1
    if(counter[ss[0]][ss[1]][1]==0):
      fname=str(str(ss[0])+","+str(ss[1])+".txt")
    else:
      fname=str(str(ss[0])+","+str(ss[1])+"_"+str(counter[ss[0]][ss[1]][1])+".txt")
    fp=open(fname,"a")
    fp.write("##")
    fp.write("\n")
    fp.close()
  if(counter[ss[0]][ss[1]][3]==0):
    counter[ss[0]][ss[1]][3]=1
    if(counter[ss[0]][ss[1]][1]==0):
      fname=str(str(ss[0])+","+str(ss[1])+".txt")
    else:
      fname=str(str(ss[0])+","+str(ss[1])+"_"+str(counter[ss[0]][ss[1]][1])+".txt")
    fp=open(fname,"a")
    fp.write("**")
    fp.write("\n")
    fp.close()
  if(counter[ss[0]][ss[1]][4]==0):
    counter[ss[0]][ss[1]][4]=1
    if(counter[ss[0]][ss[1]][1]==0):
      fname=str(str(ss[0])+","+str(ss[1])+".txt")
    else:
      fname=str(str(ss[0])+","+str(ss[1])+"_"+str(counter[ss[0]][ss[1]][1])+".txt")
    fp=open(fname,"a")
    fp.write("%%")
    fp.write("\n")
    fp.close()
print("All main block and overflow block files are created and saved in secondary memory")
