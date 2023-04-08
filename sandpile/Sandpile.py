import argparse

class Sandpile(object):
    DEFAULTCELL = 0
    
    def __init__(self):
        self.grid=[[self.DEFAULTCELL]]
        self.size = 1
        self.center = 0

    def addDrop(self, x, y):
        if self.grid[x][y] >= 3:
            self.grid[x][y] = 0
            if max(x, y)+1 >= self.size or min(x, y) < 0:
                self.growGrid()
                x += 1
                y += 1
            for i in [-1, 1]:
                print x, y
                self.addDrop(x+i, y)
                self.addDrop(x, y+i)
        else:
            self.grid[x][y] += 1

    def growGrid(self):
        self.size += 2
        self.center += 1
        for row in self.grid:
            row.insert(0, self.DEFAULTCELL)
            row.append(0)
        self.grid.insert(0, [self.DEFAULTCELL]*self.size)
        self.grid.append([self.DEFAULTCELL]*self.size)

    def show(self):
        for row in self.grid:
            print " ".join([str(cell) for cell in row])

    def getOptions(self):
        p = argparse.ArgumentParser()
        p.add_argument('t', metavar='N', type=int)
        return p.parse_args()

    def main(self):
        options = self.getOptions()
        for i in range(options.t):
            self.addDrop(self.center, self.center)
        self.show()

if __name__ == "__main__":
    sanpile = Sandpile()
    sanpile.main()
