class Path:
    hill_path = []
    row = 0
    col = 0
    nrows = 0

    def __init__(self, _hill):
        self.hill_path = _hill
        self.nrows = len(self.hill_path)
        self.ncols = len(self.hill_path[0])

    def __str__(self):
        return ''.join(self.hill_path[i] + "\n" for i in range(len(self.hill_path)))

    def seek(self):
        # Go right if possible: There's a col to the right, col on right hasn't been visited yet
        # col on right is at most one higher, or current col is start
        if self.col < self.ncols and \
                not 1 in [c in self.hill_path[self.row] for c in ">v<^"] and \
                (ord(self.hill_path[self.row][self.col + 1]) <= ord(self.hill_path[self.row][self.col]) + 1 or
                 self.hill_path[self.row][self.col]) == 'S':
            # Travel through this path
            path2=Path(self.hill_path)
            path2.hill_path[self.row] = path2.hill_path[self.row][:self.col + 1] + path2.hill_path[self.row][self.col + 1:]

            text = 'abcdefg'
            text = text[:1] + 'Z' + text[2:]
            print("do go right")
        else:
            print("not go right")
