import sys
import time


class Path:
    hill_path = []
    all_paths = []
    route = []
    row = 0
    col = 0
    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0
    nrows = 0
    timer = 0
    recursion_level = 0
    loop_count = 0

    def __init__(self, _hill_or_path):
        if isinstance(_hill_or_path, list):
            self.hill_path = _hill_or_path
            self.nrows = len(self.hill_path)
            self.ncols = len(self.hill_path[0])
            self.route = ["." * self.ncols for j in range(self.nrows)]
            self.find_start()
            self.row = self.start_row
            self.col = self.start_col
            self.valid = False
            self.count = 0
            self.all_paths.append(self)
            self.timer = time.perf_counter()
            self.recursion_level = [0]
            self.loop_count = [0]
        else:  # is instanceof Path
            self.hill_path = _hill_or_path.hill_path.copy()
            self.route = _hill_or_path.route.copy()
            self.all_paths = _hill_or_path.all_paths
            self.nrows = _hill_or_path.nrows
            self.ncols = _hill_or_path.ncols
            self.route = _hill_or_path.route.copy()
            self.row = _hill_or_path.row
            self.col = _hill_or_path.col
            self.valid = _hill_or_path.valid
            self.count = _hill_or_path.count
            self.all_paths.append(self)
            self.timer = _hill_or_path.timer
            self.recursion_level = _hill_or_path.recursion_level
            self.loop_count = _hill_or_path.loop_count

    def __str__(self):
        return '\n' + ''.join(self.route[i] + "\n" for i in range(len(self.route)))

    def seek(self):

        self.inc_round()

        if int(self.loop_count[0]) % 100000 == 0:
            print("Status: ", self.timeit())

        # if we are at E, this forms a valid route
        if self.hill_path[self.row][self.col] == 'E':
            self.valid = True
            print("E: ", self.row, self.col)
            print('\n'.join(self.route))
            # sys.exit(1)
            return True  # This was a valid route

        # Go right if possible:
        # There's a col to the right,
        # col on right hasn't been visited yet (route != <,>,v,^), otherwise we would end in a loop
        # col on right is at most one higher, or current col is start
        # If not possible, this is a dead end, and we try to go down instead

        # print("try right", self.row, self.col, self.hill_path[self.row][self.col])
        # a = self.not_on_edge(self.col, self.ncols - 1)
        # b = self.visited(self.route[self.row][self.col + 1])

        # c = self.is_low_enough(self.hill_path[self.row][self.col], self.hill_path[self.row][self.col + 1])

        if self.not_on_edge(self.col, self.ncols - 1) and \
                not self.visited(self.route[self.row][self.col + 1]) and \
                self.is_low_enough(self.hill_path[self.row][self.col], self.hill_path[self.row][self.col + 1]):
            # Travel right path
            path2 = Path(self)
            path2.route[self.row] = path2.route[self.row][:self.col] + ">" \
                                    + path2.route[self.row][self.col + 1:]
            path2.count += 1
            # print(''.join(path2.route[i] + "\n" for i in range(len(self.route))))
            path2.col += 1
            path2.seek()
            # print("back from try right", self.row, self.col, self.nrows, self.ncols)

        #print("try down", self.row, self.col, self.hill_path[self.row][self.col])
        if self.not_on_edge(self.row, self.nrows - 1) and \
                not self.visited(self.route[self.row + 1][self.col]) and \
                self.is_low_enough(self.hill_path[self.row][self.col], self.hill_path[self.row + 1][self.col]):
            # Travel down path
            path2 = Path(self)
            path2.route[self.row] = path2.route[self.row][:self.col] + "v" \
                                    + path2.route[self.row][self.col + 1:]
            path2.count += 1
            # print(''.join(path2.route[i] + "\n" for i in range(len(self.route))))
            path2.row += 1
            path2.seek()
            # print("back from try down", self.row, self.col, self.nrows, self.ncols)

        # print("try up", self.row, self.col, self.nrows, self.ncols)
        if self.not_on_edge(0, self.row) and \
                not self.visited(self.route[self.row - 1][self.col]) and \
                self.is_low_enough(self.hill_path[self.row][self.col], self.hill_path[self.row - 1][self.col]):
            # Travel up path
            path2 = Path(self)
            path2.route[self.row] = path2.route[self.row][:self.col] + "^" \
                                    + path2.route[self.row][self.col + 1:]
            path2.count += 1
            # print(''.join(path2.route[i] + "\n" for i in range(len(self.route))))
            path2.row -= 1
            path2.seek()
            # print("back from try up", self.row, self.col, self.nrows, self.ncols)

        # print("try left", self.row, self.col, self.nrows, self.ncols)
        if self.not_on_edge(0, self.col) and \
                not self.visited(self.route[self.row][self.col - 1]) and \
                self.is_low_enough(self.hill_path[self.row][self.col], self.hill_path[self.row][self.col - 1]):
            # Travel left path
            path2 = Path(self)
            path2.route[self.row] = path2.route[self.row][:self.col] + "<" \
                                    + path2.route[self.row][self.col + 1:]
            path2.count += 1
            # print(''.join(path2.route[i] + "\n" for i in range(len(self.route))))
            path2.col -= 1
            path2.seek()
            # print("back from try left", self.row, self.col, self.nrows, self.ncols)

        #print("dead end: ", self.row, self.col, self.nrows, self.ncols)
        self.all_paths.remove(self)
        recursion_level = self.recursion_level.pop()
        recursion_level -= 1
        self.recursion_level.append(recursion_level)
        # self.all_paths.pop()
        return False  # It was dead end

    def not_on_edge(self, _current, _limit):
        return _current < _limit

    def visited(self, _slot):
        return 1 in [c in _slot for c in ">v<^"]

    def is_low_enough(self, _cur_slot, _next_slot):
        s = _cur_slot
        h = _next_slot
        if s == 'E': s = "z"
        if s == 'S': s = "a"
        if h == 'E': h = "z"
        if h == 'S': h = "a"
        a = ord(h)
        b = ord(s)
        return ord(h) <= ord(s) + 1

    def find_start(self):
        for row in range(len(self.hill_path)):
            for col in range(len(self.hill_path[row])):
                if self.hill_path[row][col] == "S":
                    self.start_row = row
                    self.start_col = col

    def find_end(self):
        for row in range(len(self.hill_path)):
            for col in range(len(self.hill_path[row])):
                if self.hill_path[row][col] == "E":
                    self.end_row = row
                    self.end_col = col

    def timeit(self):
        now = time.perf_counter()
        dt = now - self.timer
        return "Statistics: time: " + str(dt) + ", loop: " + str(self.loop_count[0]) + ", recursion: " + \
            str(self.recursion_level[0]) + " number of all routes: " + str(len(self.all_paths))

    def inc_round(self):
        loop_count = self.loop_count.pop()
        loop_count += 1
        self.loop_count.append(loop_count)

        recursion_level = self.recursion_level.pop()
        recursion_level += 1
        self.recursion_level.append(recursion_level)
