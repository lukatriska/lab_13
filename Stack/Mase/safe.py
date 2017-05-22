def findPath(self):
    start = self._startCell.row, self._startCell.col
    end = self._exitCell.row, self._exitCell.col
    row, col = start
    lst = []
    for row in self._mazeCells.rows:  # creates list of coors to work with
        temp = []
        for item in row:
            if item is not None:
                temp.append('*')
            else:
                temp.append(' ')
        lst.append(temp)
    lst[start[0]][start[1]] = 'S'
    lst[end[0]][end[1]] = 'E'
    if lst[row][col] == 'E':
        return True
    elif lst[row][col] == '*':
        return False
    elif lst[row][col] == 'o':
        return False
    lst[row][col] = 'o'
    if ((row < len(lst) - 1 and search(row + 1, col))
        or (col > 0 and search(row, col - 1))
        or (row > 0 and search(row - 1, col))
        or (col < len(lst) - 1 and search(row, col + 1))):
        return True

    return False



# pprint(lst)
        # for row in lst:
        #     print(row)
        #     for col in row:
        #         if not self._exitFound(row, col):
        #             if self._validMove(curCell[0] - 1, curCell[1]):
        #                 curCell = curCell[0] - 1, curCell[1]
        #                 print(curCell)
        #             elif self._validMove(curCell[0] + 1, curCell[1]):
        #                 curCell = curCell[0] + 1, curCell[1]
        #                 print(curCell)
        #             elif self._validMove(curCell[0], curCell[1] - 1):
        #                 curCell = curCell[0], curCell[1] - 1
        #                 print(curCell)
        #             elif self._validMove(curCell[0], curCell[1] + 1):
        #                 curCell = curCell[0], curCell[1] + 1
        #                 print(curCell)
        #             self._markTried(curCell[0], curCell[1])
        # while True:
        # print(curCell)
        # curCell = self.move_up(curCell)
        # print(curCell)
        # curCell = self.move_down(curCell)
        # print(curCell)
        # curCell = self.move_right(curCell)
        # print(curCell)
        # if self._validMove(curCell[0] - 1, curCell[1]):
        #     while True:
        #     curCell = self.move_up(curCell)
            # while self._validMove(curCell[0] - 1, curCell[1]):
            #     curCell = self.move_up(curCell)

    def move_up(self, cell):
        if self._validMove(cell[0] - 1, cell[1]):
            self._markTried(cell[0], cell[1])
            return cell[0] - 1, cell[1]
        else:
            return cell

    def move_down(self, cell):
        if self._validMove(cell[0] + 1, cell[1]):
            self._markTried(cell[0], cell[1])
            return cell[0] + 1, cell[1]
        else:
            return cell

    def move_left(self, cell):
        self._markTried(cell[0], cell[1])
        if self._validMove(cell[0], cell[1] - 1):
           return cell[0], cell[1] - 1
        else:
            return cell

    def move_right(self, cell):
        self._markTried(cell[0], cell[1])
        if self._validMove(cell[0], cell[1] + 1):
            return cell[0], cell[1] + 1
        else:
            return cell

