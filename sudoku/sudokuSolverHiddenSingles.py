import sudokuSolverSimple, sudokuCell

class SudokuSolverHiddenSingles(sudokuSolverSimple.SudokuSolverSimple):
    CANDIDATECOUNTS = {p: 0 for p in sudokuCell.SudokuCell.ALLPOSSIBILITIES}

    def _countCellCandidates(self, cell, candidateCounts):
        if cell.isFound():
            del candidateCounts[cell.value]
        else:
            for possibility in cell.possibilities:
                if possibility in candidateCounts.keys():
                    candidateCounts[possibility] += 1        

    def hiddenSinglesBox(self, R, C):
        result = 0
        candidateCounts = self.CANDIDATECOUNTS.copy()
        for row in range(R, R + self.grid.BOX_HEIGHT):
            for col in range(C, C + self.grid.BOX_WIDTH):
                self._countCellCandidates(self.grid[row][col], candidateCounts)
        hiddenValues = [p for p in candidateCounts if candidateCounts[p] == 1]
        if not len(hiddenValues):
            return result
        #print "box", R, C, candidateCounts, hiddenValues
        for row in range(R, R + self.grid.BOX_HEIGHT):
            for col in range(C, C + self.grid.BOX_WIDTH):
                cell = self.grid[row][col]
                for n in hiddenValues:
                    if cell.isPossible(n):
                        #print R, C, cell
                        result += 1
                        self.grid.setValue(row, col, n)
                        hiddenValues.remove(n)
        return result

    def hiddenSinglesRow(self, r):
        result = 0
        candidateCounts = self.CANDIDATECOUNTS.copy()
        for cell in self.grid[r]:
            self._countCellCandidates(cell, candidateCounts)
        hiddenValues = [p for p in candidateCounts if candidateCounts[p] == 1]
        #print "row", r , candidateCounts, hiddenValues
        if  not len(hiddenValues):
            return result
        for col in range(len(self.grid[r])):
            cell = self.grid[r][col]
            for n in hiddenValues:
                if cell.isPossible(n):
                    #print cell.possibilities
                    self.grid.setValue(r, col, n)
                    hiddenValues.remove(n)
                    result += 1
        return result

    def hiddenSinglesCol(self, c):
        result = 0
        candidateCounts = self.CANDIDATECOUNTS.copy()
        for row in self.grid:
            self._countCellCandidates(row[c], candidateCounts)
        hiddenValues = [p for p in candidateCounts if candidateCounts[p] == 1]
        #print "col", c, candidateCounts, hiddenValues
        if not len(hiddenValues):
            return result
        for row in range(len(self.grid)):
            for n in hiddenValues:
                if self.grid[row][c].isPossible(n):
                    self.grid.setValue(row, c, n)
                    hiddenValues.remove(n)
                    result += 1
        return result


    def solveStep(self):
        result = super(SudokuSolverHiddenSingles, self).solveStep()
        for R in range(3):
            for C in range(3):
                self.hiddenSinglesBox(R * self.grid.BOX_HEIGHT, C * self.grid.BOX_WIDTH)
        for r in range(len(self.grid)):
            result += self.hiddenSinglesRow(r)
        for c in range(len(self.grid[0])):
            result += self.hiddenSinglesCol(c)
        return result


if __name__ == "__main__":
    SudokuSolverHiddenSingles.main()

