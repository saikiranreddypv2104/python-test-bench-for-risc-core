from modules.Resgisters import Register,pc
from modules.Instruction import Instruction
from tabulate import tabulate
from modules.state import state
import ast
class RISV_Model():
    def __init__(self) -> None:
        """
        This is a riscv simulator, this will take an object of instruction
        and try to mimic the the single cycle.
        functions:  
        simulate      ->Simulate the current instructions.
        display state ->display the current state of the registers.
        return state  ->returns an object with the state information for scoreboard
        """
        self.registerMemory=Register(n=32)
        self.pc=pc()
        self.dataMemory=Register(1000)
        self.instruction=None
    def reset(self):
        self.dataMemory.reset()
        self.registerMemory.reset()
        self.pc.reset()
        
    def simulate(self,instruction:Instruction)->None:
        """
        This fucntion takes an instruction of type Instruction , and try to guess the next class
        """
        self.instruction=instruction
        #print(f"simulate function is called")
        #print(f"opcode ={instruction.opcode} rd={instruction.rd}  rs1={instruction.rs1} rs2={instruction.rs2}")
        if instruction.type=="R":
            rs1_data=getattr(self.registerMemory,f"register_{instruction.rs1}")
            rs2_data=getattr(self.registerMemory,f"register_{instruction.rs2}")
            if instruction.funct7==2 :# SUB
                rd_data=rs1_data-rs2_data
            elif instruction.funct3==0:# ADD
                rd_data=rs1_data+rs2_data
            elif instruction.funct3==1:# SLL
                print(f"rs1={rs1_data},loc={instruction.rs1} rs2={rs2_data},loc={instruction.rs2}  instruction={self.instruction}")
                try:
                    print(f"register memory :\n{self.registerMemory}")
                except Exception as e:
                    print(f"error during the printing the register inside the simulatem{e}")
                rd_data=rs1_data<<rs2_data
            elif instruction.funct3==2:# SLT
                if rs1_data<rs2_data:
                    rd_data=1
                else:
                    rd_data=0
            elif instruction.funct3==4:# XOR
                rd_data=rs1_data^rs2_data
            elif instruction.funct3==6:# OR
                rd_data=rs1_data|rs2_data
            elif instruction.funct3==7:# AND
                rd_data=rs1_data&rs2_data
            #print(f"before set ={getattr(self.registerMemory,f"register_{instruction.rd}")}")
            setattr(self.registerMemory,f"register_{instruction.rd}",rd_data)
            #print(f"after set ={getattr(self.registerMemory,f"register_{instruction.rd}")}")
        elif instruction.type=="I":
            rs1=getattr(self.registerMemory,f"register_{instruction.rs1}")

            if instruction.funct3==0:# ADD
                rd=rs1+instruction.immediate
            elif instruction.funct3==1:# SLL
                rd=rs1<<instruction.immediate
            elif instruction.funct3==2:# SLT
                if rs1<instruction.immediate:
                    rd=1
                else:
                    rd=0
            elif instruction.funct3==4:# XOR
                rd=rs1^instruction.immediate
            elif instruction.funct3==6:# OR
                rd=rs1|instruction.immediate
            elif instruction.funct3==7:# AND
                rd=rs1&instruction.immediate
            setattr(self.registerMemory,f"register_{instruction.rd}",rd)
        
        elif instruction.type=="L":
            rs1=getattr(self.registerMemory,f"register_{instruction.rs1}")
            memory=rs1+instruction.immediate
            data=getattr(self.dataMemory,f"register_{memory}")
            setattr(self.registerMemory,f"register_{instruction.rd}",data)
        
        elif instruction.type=='S':
            rs1=getattr(self.registerMemory,f"register_{instruction.rs1}")
            rs2=getattr(self.registerMemory,f"register_{instruction.rs2}")
            memory=rs1+instruction.immediate
            setattr(self.dataMemory,f"register_{memory}",rs2)
            
        else:
            print(f"Instruction is not supported given type ={instruction.type}")
        self.pc.PC+=4
    def display_pc(self):
        print(f"pc={self.pc}")
    def display_registerMemory(self):
        
        l=[]
        print(f"Register Memory")
        for i in range(0,32):
            l.append([ f"register_{i}",getattr(self.registerMemory,f"register_{i}") ])
        print(tabulate(l,tablefmt="grid"))
    def display_dataMemory(self):
        l=[]
        print(f"Data Memory:")
        for i in range(0,100):
            l.append([ f"data_{i}",getattr(self.dataMemory,f"register_{i}") ])
        print(tabulate(l,tablefmt="grid"))
    
    def state(self):
        x=state()
        x.register_memory=self.registerMemory
        x.data_memory=self.dataMemory
        x.instruction=self.instruction.hexcode.zfill(8)
        x.pc=self.pc.PC
        return x
    def analysis(self):
        f=open("RTL/decoder.v","r")
        s=f.read()
        f.close()
        ss = ast.literal_eval(s)
        return list(ss)
    
    