class IntCode:
    def __init__(self, data):
        self.func_dict = {1: self.add, 2: self.mult}
        self.memory = data
        self.active_idx = 0

    def add(self):
        idx_one = self.memory[self.active_idx + 1]
        idx_two = self.memory[self.active_idx + 2]
        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]
        dest = self.memory[self.active_idx + 3]
        self.memory[dest] = val_two + val_one
        self.active_idx += 4

    def mult(self):
        idx_one = self.memory[self.active_idx + 1]
        idx_two = self.memory[self.active_idx + 2]
        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]
        dest = self.memory[self.active_idx + 3]
        self.memory[dest] = val_one * val_two
        self.active_idx += 4

    def run(self):
        cur_op = self.memory[self.active_idx]
        while cur_op != 99:
            self.func_dict[cur_op]()
            cur_op = self.memory[self.active_idx]


    def get_pos_value(self, idx):
        return self.memory[idx]
