class MOS6502:
    def __init__(self):
        self.reset()

    def reset(self):
        self.reg_a = 0x00
        self.reg_x = 0x00
        self.reg_y = 0x00
        self.reg_pc = 0x0000
        self.reg_sp = 0x0000

        self.flag_c = False
        self.flag_z = False
        self.flag_i = False
        self.flag_d = False
        self.flag_b = False
        self.flag_r = True
        self.flag_v = False
        self.flag_n = False
