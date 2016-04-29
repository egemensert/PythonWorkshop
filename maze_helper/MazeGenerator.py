import random

def dist((x1,y1),(x2,y2)):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

class MazeGenerator:
    compass = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
               (1, 1), (1, 0), (1, -1), (0, -1)]

    title = ["NW", "N", "NE","E","SE","S","SW","W"]

    def __init__(self,i, j, obs_density, min_dist,max_cost,f=None):
        self.ROW = [k for k in range(i)]
        self.COLUMN = [k for k in range(j)]
        self.MAX_COST = max_cost
        self.MIN_DIST = (min_dist + (1-min_dist)*random.random())*min(i,j)
        self.FROM_I, self.FROM_J = None,None
        self.TO_I, self.TO_J = None,None
        self.density = obs_density
        self.maze,self.maze_costs = self.__generate_maze()
        if f:
            self.__writeToFile(f)

    def getMazes(self):
        return self.maze, self.maze_costs

    def __generate_maze(self):
        maze = [[[] for j in self.COLUMN] for i in self.ROW]
        maze_costs = [[["X" for j in self.COLUMN] for i in self.ROW] for k in self.title]
        for i in self.ROW:
            for j in self.COLUMN:
                q = random.random()
                if q >= self.density:
                    q = 0
                else:
                    q = 1
                maze[i][j] = q

        for i in self.ROW:
            for j in self.COLUMN:
                for k in range(len(self.compass)):
                    ci,cj = self.compass[k]
                    if len(self.COLUMN)>ci+i>=0 and len(self.ROW)>cj+j>=0 and maze[ci+i][cj+j] == 1:
                        maze_costs[k][i][j] =random.randint(0,self.MAX_COST)

        i,j = False,False

        while not (i and j):
            i1,i2 = random.randint(0,len(self.ROW) -1), random.randint(0,len(self.ROW) -1)
            j1,j2 = random.randint(0,len(self.COLUMN) -1), random.randint(0,len(self.COLUMN) -1)

            if maze[i1][j1] and maze[i2][j2] and dist((i1,j1),(i2,j2)) > self.MIN_DIST:
                self.FROM_I, self.FROM_J = (i1,j1)
                self.TO_I, self.TO_J = (i2,j2)
                break

        return maze,maze_costs

    def __writeToFile(self,file):
        with open(file,"w+") as f:
            f.write(str(len(self.ROW)) + " " +str(len(self.COLUMN))+"\n")
            f.write(str(self.FROM_I) + " " +str(self.FROM_J)+"\n")
            f.write(str(self.TO_I) + " " +str(self.TO_J)+"\n")

            for i in range(len(self.title)):
                f.write(self.title[i]+"\n")
                m = self.maze_costs[i]
                for row in m:
                    foo = " ".join(map(str,row))
                    f.write(foo+"\n")


