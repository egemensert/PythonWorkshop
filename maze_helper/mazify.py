from main import Maze
from MazeGenerator import MazeGenerator
from MazeVisualizer import MazeVisualizer
import sys,time


i, j, obs_density, min_dist,max_cost = tuple(map(float,sys.argv[1][1:-1].split(",")))
flag = False
if sys.argv[2] ==  "true":
    flag = True
if len(sys.argv) > 3:
    FILEPATH = sys.argv[3]
else:
    FILEPATH = None

maze = MazeGenerator(int(i),int(j),obs_density,min_dist,max_cost,f=FILEPATH)

print "Maze is generated."

paths = [["BFS",0],["DFS",1],["Uniform Search",2],["Iteratively Deepening DFS",3],["Best First Search",4],
         ["A* Search with Heuristics: 0", 5,0],["A* Search with Heuristics: 1",5,1],["A* Search with Heuristics: 2",5,2]]

for i in range(len(paths)):
    path = paths[i]
    h = 1
    s = path[1]
    if s == 5:
        h = path[2]
        del path[2]
    init = time.time()
    res =Maze(FILEPATH,s,h)
    t = round(time.time()-init,4)
    paths[i][1] = res.path

    paths[i] = (paths[i][0] + "\nPath Cost: %s\nRuntime: %sms" % (res.cost,t),tuple(paths[i][1]))
    paths[i] = tuple(paths[i])




print "Paths are calculated."

MazeVisualizer(maze,FILEPATH,paths=paths,show=flag)

# path = map(tuple,path.split("-"))