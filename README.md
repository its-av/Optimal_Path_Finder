# Optimal_Path_Finder
Shortest path algorithm on Partitioned Graph 

This implementation is a memory efficient way of calculating shortest distances between vertices in large real life datasets 
  of road network. Here we keep only that partition of graph in main memory that contain node which is getting processed, hence we 
  are saved from trouble of storing entire graph at once in main memory. Unused partitions remain in secondary memory.

Before running the code again make sure you delete all previously generated txt files. 

To run the code
>> Open the terminal from the location where all .py file exists
>> type "python 2021AIM1004.py"

After the partitioning we get all the main disk block and overflow disk block .txt's in the same folder where .py file was located
We also get a user menu
>>"Enter 1 for Normal Dijkestra"
>>"Enter 2 for Dijkestra on grids"
>>"Enter -1 to exit"

Note:- Node IDs will start from 0 and will increment 1 by one i.e 0,1,2,3... in the "nodes.txt"

