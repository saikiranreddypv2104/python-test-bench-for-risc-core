import cocotb
from modules.Resgisters import Register
from logging import warning,error,info
class state():
    def __init__(self) -> None:
        self.dut=cocotb.top
        self.register_memory=self.peek_register_memory(self.dut)
        self.data_memory=self.peek_data_memory(self.dut)
        self.instruction,self.pc=self.peek_pc_instruction(self.dut)
    def peek_data_memory(self,dut):
        """
        This fucntion takes a snapshot of the  data mmemory
        of size 100
        """
        register=Register(1000)
        for i in range(1000):
            x=dut.dataPath.data_Mem.memory[i].value
            setattr(register,f"register_{i}",int(x))
        return register
    def peek_register_memory(self,dut):
        """ 
        This fucntion take a snapshot of the registers that point as stores in the register memory
        """
        register=Register(32)
        for i in range(32):
            x=dut.dataPath.reg_mem.memory[i].value
            setattr(register,f"register_{i}",int(x))
        return register
    def peek_pc_instruction(self,dut):
        inst = dut.dataPath.instruction.value
        pc=self.dut.dataPath.pc.value
        if 'x' in str(inst):
            instruction='x'*8
        elif 'z' in str(inst):
            instruction='z'*8
        else:
            instruction=hex(int(str(inst),2))[2:].zfill(8)
        if 'x' in str(pc):
            pc='x'
        elif 'z' in str(pc):
            pc='z'
        else:
            pc=hex(int(str(pc),2))[2:]

        return instruction,pc


    def __str__(self) -> str:
        return f"\n\ninstruction ={self.instruction} pc={self.pc}\n"+f"Register memory:\n{self.register_memory}\n"+f"data Memory:\n{self.data_memory}\n"
        
    def __eq__(self, value: object) -> bool:
        print((f"{self.instruction}== {value.instruction}"))
        inst_true=(self.instruction==value.instruction)
        reg_true=(self.register_memory==value.register_memory)
        data_true=(self.data_memory==value.data_memory)
        if inst_true and reg_true and data_true:
            return True
        else:
            print(f"instruction match : {inst_true}\nregister match :{reg_true}\ndata match :{data_true}")
            return False