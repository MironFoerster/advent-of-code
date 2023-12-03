class Grid():
    def __init__(self, lines, oob = "."):
        self.cols = len(lines[0])
        self.max_x = self.cols - 1
        self.rows = len(lines)
        self.max_y = self.rows - 1
        self.flat = "".join(lines)
        self.lines = lines
        self.oob = oob

    def is_inbound(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def coord_from_flat_index(self, index):
        return index % self.rows , index // self.rows

    def move_r_from(self, x, y):
        x += 1
        return x, y, self.lines[y][x] if self.is_inbound(x, y) else self.oob

    def move_l_from(self, x, y):
        x -= 1
        return x, y, self.lines[y][x] if self.is_inbound(x, y) else self.oob
    
    def move_u_from(self, x, y):
        y -= 1
        return x, y, self.lines[y][x] if self.is_inbound(x, y) else self.oob
    
    def move_d_from(self, x, y):
        y += 1
        return x, y, self.lines[y][x] if self.is_inbound(x, y) else self.oob


class WrappingGrid():
    def __init__(self, lines, oob = "."):
        self.cols = len(lines[0])
        self.rows = len(lines)
        self.max_pos = self.cols * self.rows - 1
        self.flat = "".join(lines)
        self.lines = lines
        self.oob = oob
    
    def is_inbound(self, position):
        return 0 <= position <= self.max_pos

    def move_r_from(self, position):
        if self.is_inbound(position + 1):
            return position + 1, self.flat[position+1]
        else:
            return position + 1, self.oob

    
    def move_l_from(self, position):
        if self.is_inbound(position - 1):
            return position - 1, self.flat[position-1]
        else:
            return position - 1, self.oob
    
    def move_u_from(self, position):
        if self.is_inbound(position - self.cols):
            return position - self.cols, self.flat[position-self.cols]
        else:
            return position - self.cols, self.oob
    
    def move_d_from(self, position):
        if self.is_inbound(position + self.cols):
            return position + self.cols, self.flat[position+self.cols]
        else:
            return position + self.cols, self.oob

