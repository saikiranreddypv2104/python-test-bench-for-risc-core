from tabulate import tabulate
from logging import info
class Register():
    """
    To simulate the registers
    """
    def __init__(self,n) -> None:
        self.reg_count=n
        for i in range(n):
            setattr(self,f"register_{i}",i)
        self.register_0 = 0

    def __str__(self) -> str:
        s=[["\033[92m"+"Regsiter_number"+"\033[0m","\033[92m"+"decimal_value"+"\033[0m","\033[92m"+"binary_value"+"\033[0m"]]
        for i in range(self.reg_count):
            value=getattr(self,f"register_{i}") 
            s.append([f"register_{i}",value,format(value,'032b')])

        return tabulate(s,tablefmt="grid")
       
    
    def __eq__(self,other):
        if self.reg_count==32: reg_type="Register MEmory"
        else: reg_type="Data_memory"
        x=True
        for i in range(self.reg_count):
            if getattr(self,f"register_{i}")!=getattr(other,f"register_{i}"):
                info("\033[92m"+f"register missmatch ,type : {reg_type} \n\t\taddress:{i} \n\t\tvalues :[{getattr(self,f"register_{i}")},{getattr(other,f"register_{i}")}]"+"\033[0m")
                x=False
        return x
    def reset(self):
        l=[]
        for i in range(self.reg_count):
            setattr(self,f"register_{i}",0)




class pc():
    """
    To Hold pc Value
    """
    def __init__(self) -> None:
        self.PC=0
    def reset(self):
        self.PC=0
    def __str__(self) -> str:
        """
        returns the values of the PC
        """
        return f"{self.PC}"

    def __eq__(self, value: object) -> bool:
        """
        To compare two objects
        """
        return self.PC == value.PC



        
        