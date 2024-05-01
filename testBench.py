from queue import Queue as fifo
import cocotb
import cocotb.triggers
import pyuvm
from pyuvm import *
from cocotb.clock import Clock
from cocotb import start_soon
from cocotb.triggers import ClockCycles,RisingEdge,FallingEdge
from modules.Instruction import Instruction
from modules.Resgisters import Register
from logging import info,warning
from modules.state import state
from modules.simulator import  RISV_Model
from tabulate import tabulate


class engine(metaclass=pyuvm.Singleton):
    def __init__(self,n) -> None:
        self.insruction_fifo=fifo()# is for sending the instructions to the 
        self.actual_state_fifo=fifo()
        self.simulated_state_fifo=fifo()
        self.n=n
        self.dut=cocotb.top
        self.cpi=1
        self.model=RISV_Model()
        self.coverage={
            "add":0,
            "xor":0,
            "or":0,
            "and":0,
            "slt":0,
            "addi":0,
            "xori":0,
            "ori":0,
            "andi":0,
            "slti":0,
            "load":0,
            "store":0

        }

    def set_instruction(self,type_in="R"):
        path_to_instruction_memory_file ="RTL/instruction.mem"
        path_to_instruction_text_file="instruction file.txt"
        ins_file=open(path_to_instruction_memory_file,"w+")
        instruction_file=open(path_to_instruction_text_file,"w+")
        for i in range(self.n):
            x=Instruction(type_in)
            ins_file.write(x.hexcode.zfill(8))
            ins_file.write("\n00000000\n00000000\n00000000\n")
            instruction_file.write(str(x))
            self.insruction_fifo.put(x)
        ins_file.close()
        instruction_file.close()
        return True
    

    async def check(self):
        print(f"inside the check fucntion")
        f=open("check.txt","w+")
        count=0
        while True:
            count=count+1
            await RisingEdge(self.dut.clk)
            x=state()
            print(f"checking isntrcution={(x.instruction)}")
            if 'x'  in str(x.instruction):
                break
            f.write(str(x.instruction))
            f.write("\n")
            self.actual_state_fifo.put(x)
        f.close()

    async def scoreboard(self):
        model = self.model
        print("\033[92m"+f"inside the scoreboard")
        print(f"size of the fifo is instruction={self.insruction_fifo.qsize()}\nactual ={self.actual_state_fifo.qsize()}\n")
        self.score=0

        while True:
            # Check FIFO emptiness before getting data
            if self.insruction_fifo.empty() and self.actual_state_fifo.empty():
                break  # Exit loop if either FIFO is empty

            await RisingEdge(self.dut.clk)
            instruction =  self.insruction_fifo.get()
            model.simulate(instruction)
            expected = model.state()
            self.model=model
            actual =  self.actual_state_fifo.get()#TODO
            self.updateCoverage(instruction)
            print(instruction)
            print(f"expected ={expected.instruction}")
            print(f"actual instruction={actual.instruction}")
            print(f"\nis actual and predicted are same : {actual==expected}\n")
            print(str(model))
            #print(f"expected reg memory:\n{expected.register_memory}")
            #print(f"actual reg memory:\n{actual.register_memory}")
            if actual==expected :
                self.score+=1
            else:
                memory=instruction.rs1+instruction.immediate
                print(f"\033[92m"+f"instruction address = {memory}"+"\033[0m")
                print(f"\033[92m"+f"simulator : {getattr(expected.data_memory,f"register_{memory}")}  actual : {getattr(actual.data_memory,f"register_{memory}")}"+"\033[0m")
        
        print("\033[92m"+f"score={self.score}"+"\033[0m")
    def end(self):
        s=self.analysis()
        stri=tabulate(s,tablefmt="grid")
        print(f"Performance Analysis:")
        print(stri)
        # Convert dictionary items to list of tuples, filtering out values greater than 0
        table = [(key, value) for key, value in self.coverage.items() if value > 0]

        # Print the table
        print(f"Coverage report:")
        print(tabulate(table, headers=["Key", "Value"], tablefmt="grid"))

        print(f"success={self.score}, total send={1000}")
        
    async def start_clock_and_reset(self):
        dut=self.dut
        clk= Clock(dut.clk,10,units="us")
        cocotb.start_soon(clk.start())
        dut.reset.value=1
        await ClockCycles(dut.clk,2)
        dut.reset.value=0
        warning(f"clock is created and reset is done")

    def updateCoverage(self,instruction):
        if instruction.opcode==51:
            if instruction.funct3==0:self.coverage["add"]+=1
            elif instruction.funct3==4:self.coverage["xor"]+=1
            elif instruction.funct3==6:self.coverage["or"]+=1
            elif instruction.funct3==7:self.coverage["and"]+=1
            elif instruction.funct3==2:self.coverage["slt"]+=1
        elif instruction.opcode==19:
            if instruction.funct3==0:self.coverage["addi"]+=1
            elif instruction.funct3==4:self.coverage["xori"]+=1
            elif instruction.funct3==6:self.coverage["ori"]+=1
            elif instruction.funct3==7:self.coverage["andi"]+=1
            elif instruction.funct3==2:self.coverage["slti"]+=1
        elif instruction.opcode==35:self.coverage["store"]+=1
        elif instruction.opcode==3:self.coverage["load"]+=1
    def analysis(self):
        score=self.score
        cpi=self.cpi
        fclock=40*(10**6)
        mips=lambda fclock,cpi:fclock/(cpi*10**6)
        t =lambda n,cpi,fclock:(n*cpi)/fclock
        s= [["Number of instructions(n)",f"{score}"],
        ["Cycles per Instructions(CPI)" , f"{cpi}"],
        ["Instructions Per Cycle(IPC)",f"{cpi}"],
        ["Clock frequency",f"{fclock}"],
        ["Throughput","1"],
        ["Execution Time",f"{t(score,cpi,fclock)}"],
        ["MIPS Execution",f"{mips(fclock,cpi)}"]
        ]
        return s

        
@cocotb.test()
async def RiscV_Test(dut):
    slave=engine(n=200)
    slave.set_instruction("L")
    await slave.start_clock_and_reset()
    cocotb.start_soon(slave.check())
    await ClockCycles(dut.clk,9998,True) #998
    await slave.scoreboard()
    slave.end()

