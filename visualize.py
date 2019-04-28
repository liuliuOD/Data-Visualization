import matplotlib.pyplot as plt
class visualize () :
#    def __init__ (self) :

        
    def scatter (self, x, y, color = 'g', marker = 'o', size = 8) :
        plt.scatter(x, y, c = color, marker = marker, s = size)
        
        return self
    
#     def plot (self, x, y, color = 'g') :
#         plt.plot(x, y, color = color, marker = marker)
    
#         return self
    
    def show (self) :
        plt.show()
    
        return self

    def draw (self) :
        plt.draw()
    
        return self

    def pause (self, pauseZone = 0.1) :
        plt.pause(pauseZone)

        return self
    
    def close (self, window = "all") :
        plt.close(window)

        return self

    def interactive (self, turn = True) :
        if turn :
            plt.ion()
        else :
            plt.ioff()

        return self

    def clearWindow (self) :
        plt.clf()

        return self

    def save (self, imgName = "test.png") :
        plt.savefig(imgName)

        return self
