import rom
import config

class memory:
    def __init__(self):
        self.ram = [0x00] * config.ramsize

    def read(address):
        # read ram
        if address >= 0x0000 and address <= config.ramsize:
            begin_ram = 0x0000
            offseted_address = address - begin_ram
            return memory.ram[offseted_address]
        # read wozmon
        if address  >= 0xff00 and address <= 0xffff:
            begin_wozmon = 0xff00
            offseted_address = address - begin_wozmon
            return rom.wozmon[offseted_address]
        
        
    def write(address, data):
        return 0