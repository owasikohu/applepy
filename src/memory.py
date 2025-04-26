import bios
import config

class memory:
    def __init__(self):
        self.ram = [0x00] * config.ramsize
    
    def read_memory(address):
        if address  >= 0xff00:
            begin_wozmon = 0xff00
            offseted_address = address - begin_wozmon
            return bios.wozmon[offseted_address]
        
        
    def write_memory(address, data):
        return 0