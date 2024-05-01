from random import randint
import random
import tabulate
class Instruction():
    """
    The Instrcution class is create to handle all functions of an instruction.That 
    includes 
        - Instruction generation based on type, in hexcode format.
        - Instruction decode , converts into asm language.
    """
    def __init__(self,Instruction_type="R") -> None:
        """
        The constructor takes the type as an input.By Default we take R-type
        The valid values of type are 
            R type -->"R"\n
            I type -->"I"\n
            B type -->"B"\n
            I type --->"S"\n
            Load   --->"L"\n
            store  --->"S"\n
            Hexcode is stored in hexcode, and assembly code is stored in assembly code
        """
        if Instruction_type=="": Instruction_type="R"
        self.type=Instruction_type
        self.funct7=None
        self.funct3=None
        self.opcode=None
        self.rs1=None
        self.rs2=None
        self.rd=None
        self.immediate=None
        self.hexcode=None
        self.randomize()

    def randomize(self):
        if (self.type=="R"):
            #This case is for creating the Rtype instructions
            self.rs1=self.generate_random_register()
            self.rs2=self.generate_random_register()
            self.rd=self.generate_random_register()
            self.funct3 = random.choice([0,2,4,6,7])#removed funct3=1 value because its shit
            self.funct7= random.choice([0]) if(self.funct3==0) else 0#add 2 for subtraction
            self.opcode=51
            hexcode=format(self.funct7,'07b')+format(self.rs2,'05b')+format(self.rs1,'05b')+format(self.funct3,'03b')+format(self.rd,'05b')+format(self.opcode,'07b')
            self.hexcode=hex(int(hexcode,2))[2:]
        elif self.type=="I":
            #This case is for creating the I type instructions
            self.rs1=self.generate_random_register()
            self.rd=self.generate_random_register()
            self.immediate=randint(0,2**4)
            self.funct3 = random.choice([0,2,4,6,7])#TODO removing the sll deal later 1
            self.opcode=19
            hexcode=format(self.immediate,'012b')+format(self.rs1,'05b')+format(self.funct3,'03b')+format(self.rd,'05b')+format(self.opcode,'07b')
            self.hexcode=hex(int(hexcode,2))[2:]
        elif self.type=="L":
            #This case is for creating the Load type instructions
            self.rs1=self.generate_random_register()
            self.rd=self.generate_random_register()
            self.immediate=randint(0,2**4)
            self.funct3 = 2
            self.opcode=3
            hexcode=format(self.immediate,'012b')+format(self.rs1,'05b')+format(self.funct3,'03b')+format(self.rd,'05b')+format(self.opcode,'07b')
            self.hexcode=hex(int(hexcode,2))[2:] 
        elif self.type=="S":
            #This case is for creating the Store type instructions
            self.rs1=self.generate_random_register()
            self.rs2=self.generate_random_register()
            self.immediate=randint(0,2**4)
            self.funct3 = 2
            self.opcode= 35
            imm=format(self.immediate,'012b')
            hexcode=imm[:7]+format(self.rs2,'05b')+format(self.rs1,'05b')+format(self.funct3,'03b')+imm[7:]+format(self.opcode,'07b')
            self.hexcode=hex(int(hexcode,2))[2:]

    def generate_random_register(self):
        number=randint(1,31)
        return number
    def display(self):
            s=self.generate_data_list()
            hexcode=str(self.hexcode).zfill(8)
            x=f"\ntype={self.type}\n"+tabulate.tabulate(s,tablefmt="grid",showindex=True)+f"\n hexcode ={hexcode}"
            print(x)
            return x
    def __str__(self):
            s=self.generate_data_list()
            hexcode=str(self.hexcode).zfill(8)
            x=f"\ntype={self.type}\n"+tabulate.tabulate(s,tablefmt="grid",showindex=True)+f"\n hexcode ={hexcode}"
            return x
    def generate_data_list(self)->list:
        """
        generatea list with relevent data for each type of instruction
        """
        if self.type=="R":
              s=[["Name","decimal","Binary"],
                  ["opcode",self.opcode,format(self.opcode,'07b')],
                 ["fucnt7",self.funct7,format(self.funct7,'03b')],
                 ["fucnt3",self.funct3,format(self.funct3,'03b')],
                 ["rs1",self.rs1,format(self.rs1,'05b')],
                 ["rs2",self.rs2,format(self.rs2,'05b')],
                 ["rd",self.rd,format(self.rd,'05b')],
                 ]
        elif self.type=="I" or self.type=="L":
            s=[["Name","decimal","Binary"],
                 ["opcode",self.opcode,format(self.opcode,'07b')],
                 ["fucnt3",self.funct3,format(self.funct3,'03b')],
                 ["rs1",self.rs1,format(self.rs1,'05b')],
                 ["rd",self.rd,format(self.rd,'05b')],
                 ["imm",self.immediate,format(self.immediate,'012b')]
                 ]
        elif self.type=="S":
            s=[["Name","decimal","Binary"],
                ["opcode",self.opcode,format(self.opcode,'07b')],
                 ["fucnt3",self.funct3,format(self.funct3,'03b')],
                 ["rs1",self.rs1,format(self.rs1,'05b')],
                 ["rs2",self.rs2,format(self.rs2,'05b')],
                 ["imm",self.immediate,format(self.immediate,'012b')]
                 ]
        return s


