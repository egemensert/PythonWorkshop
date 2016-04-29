import MazeGenerator
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

class MazeVisualizer():
    def __init__(self,this,filename,paths=None,show=False):
        self.paths = paths
        if paths:
            self.n = len(paths)+1
        else:
            self.n = 1
        self.f,self.plots = plt.subplots(3,3,sharex=True,sharey=True)
        # self.f.suptitle("Paths and Costs")
        plt.xlim(-0.5,len(this.ROW)-0.5)
        plt.ylim(-0.5,len(this.COLUMN)-0.5)
        c=0
        for qr in range(3):
            for qc in range(3):
                c+=1
                p = self.plots[qc][qr]
                for i in this.ROW:
                    for j in this.COLUMN:
                        # currentAxis = self.f.gca()
                        if this.maze[i][j] == 0:
                            clr = "black"
                        else:
                            clr = "white"
                        p.add_patch(Rectangle((i- .5, j- .5), 1, 1, facecolor=clr))
                        # p.plot(i,j,"r.",alpha=0.2)

                p.add_patch(Rectangle((this.FROM_I - .5, this.FROM_J- .5), 1, 1, facecolor="green"))
                p.add_patch(Rectangle((this.TO_I - .5, this.TO_J- .5), 1, 1, facecolor="red"))

                print "Plot %i has been prepared." % (c)
        self.plots[0][0].set_title("Main Maze")
        if paths:
            self.__draw_path()


        plt.subplots_adjust( hspace=0.5)
        plt.savefig(filename.split(".")[0]+'.svg', format='svg', dpi=1200)

        if show:
            plt.show()

    def __draw_path(self):
        # print enumerate(self.paths)
        for i,(title,path) in enumerate(self.paths):
            current_plot = self.plots[2-i/3][-(i+1)%3]
            # currentAxis = current_plot.gca()
            current_plot.set_title(title,fontsize=8)
            for x,y in path:
                current_plot.add_patch(Rectangle((x- .5, y- .5), 1, 1, facecolor="blue",alpha=0.8))

            print title," has been drawn"

