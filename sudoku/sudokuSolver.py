
import argparse, sudokuGrid

class SolveFailedException(Exception):
    pass

class SudokuSolver(object):
    STEPFAILLIMIT = 9

    def __init__(self, fileName, failLimit = STEPFAILLIMIT):
        self.grid = sudokuGrid.SudokuGrid.loadFile(fileName)
        self.failLimit = failLimit
        self.failedSteps = 0

    def checkSolution(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                value = self.grid[r][c].value
                if value == None:
                    continue
                for R in range(len(self.grid)):
                    if R == r:
                        continue
                    if self.grid[R][c].value == value:
                        print r, c, "matches", R, c
                        return False
                for C in range(len(self.grid[r])):
                    if C == c:
                        continue
                    if self.grid[r][C].value == value:
                        print r, c, "matches", r, C
                        return False
        return True

    def solveStep(self):
        return False

    def solve(self):
        while not self.grid.isComplete():
            if self.solveStep():
                #print self.grid
                self.failedSteps = 0
            else:
                self.failedSteps += 1
                if self.failedSteps >= self.failLimit:
                    raise SolveFailedException, "Couldn't find any more moves toward solution."
            if not self.checkSolution():
                raise SolveFailedException, "Given Solution Invalid."

    @staticmethod
    def args():
        parser = argparse.ArgumentParser()
        parser.add_argument("filename", type = str, help = "name of a sudoku file to solve")
        parser.add_argument("-l", "--limit", type = int, help = "limit attempted steps before solve attempt is counted as failure")
        return parser.parse_args()

    @classmethod
    def main(self):
        args = self.args()
        solver = self(args.filename, args.limit)
        try:
            solver.solve()
            if not solver.checkSolution():
                raise SolveFailedException, "Given Solution Invalid."
            print solver.grid
        except KeyboardInterrupt:
            print "User exit."
        except SolveFailedException as err:
            print solver.grid
            print err.message
