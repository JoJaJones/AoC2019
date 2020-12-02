class IntCode:
    def __init__(self, data, input_val=None):
        self.func_dict = {1: self.add, 2: self.mult, 3: self.get_input, 4: self.output,
                          5: self.jump_true, 6: self.jump_false, 7: self.less_than, 8: self.equals}
        self.memory = data
        self.active_idx = 0
        self.current_opcode = self.memory[self.active_idx]
        self.input_val = input_val
        self.output_val = None

    def get_idx(self, idx, position_mode = True):
        if position_mode:
            return self.memory[idx]
        else:
            return idx

    def add(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = val_two + val_one
        self.active_idx += 4

    def mult(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = val_one * val_two
        self.active_idx += 4

    def run(self):
        cur_op = self.memory[self.active_idx]
        while cur_op != 99:
            self.func_dict[cur_op]()
            cur_op = self.memory[self.active_idx]

    def get_input(self):
        dest = self.load_indices(1)[0]
        if self.input_val is None:
            self.input_val = int(input("input: "))

        self.memory[dest] = self.input_val
        self.input_val = None
        self.active_idx += 2

    def output(self):
        dest = self.load_indices(1)[0]

        self.output_val = self.memory[dest]
        print(self.output_val)
        self.active_idx += 2

    def jump_true(self):
        bool_idx, dest = self.load_indices(2)
        if self.memory[bool_idx] != 0:
            self.active_idx = self.memory[dest]
        else:
            self.active_idx += 3

    def jump_false(self):
        bool_idx, dest = self.load_indices(2)

        if self.memory[bool_idx] == 0:
            self.active_idx = self.memory[dest]
        else:
            self.active_idx += 3

    def less_than(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = 1 if val_one < val_two else 0
        self.active_idx += 4

    def equals(self):
        idx_one, idx_two, dest = self.load_indices(3)

        val_one = self.memory[idx_one]
        val_two = self.memory[idx_two]

        self.memory[dest] = 1 if val_one == val_two else 0
        self.active_idx += 4

    def load_parameter_modes(self, length=5):
        opcode = str(self.current_opcode)
        while len(opcode) < length:
            opcode = "0" + opcode
        opcode = opcode[:-2]
        modes = []
        while len(opcode) > 0:
            modes.append(opcode[-1] == "0")
            opcode = opcode[:-1]

        return modes

    def load_indices(self, num_to_load):
        modes = self.load_parameter_modes(num_to_load + 2)
        indices = []
        shift = 1
        while len(modes) > 0:
            indices.append(self.get_idx(self.active_idx + shift, modes.pop(0)))
            shift += 1

        return indices

    def run(self):
        while self.current_opcode != 99:
            currop = int(str(self.current_opcode)[-2:])
            self.func_dict[currop]()
            self.current_opcode = self.memory[self.active_idx]

        return self.output_val

    def get_pos_value(self, idx):
        return self.memory[idx]
