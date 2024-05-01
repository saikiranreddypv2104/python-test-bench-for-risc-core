class helper():
    def __init__(self) -> None:
        self.R_type={
            "ADD":{
                "funct7":"0000000",
                "funct3":"000"
            },
            "SLT":{
                "funct7":"0000000",
                "funct3":"010"
            },
            "AND":{
                "funct7":"0000000",
                "funct3":"111"
            },
            "OR":{
                "funct7":"0000000",
                "funct3":"110"
            },
            "XOR":{
                "funct7":"0000000",
                "funct3":"100"
            },
            "SLL":{
                "funct7":"0000000",
                "funct3":"001"
            },
            "SUB":{
                "funct7":"0100000",
                "funct3":"000"
            },

        }
        self.I_type={
            "ADDI":{
                "funct3":"000"
            },
            "XORI":{
                "funct3":"100"
            },
            "ORI":{
                "funct3":"110"
            },
            "ANDI":{
                "funct3":"111"
            },
            "SLTI":{
                "funct3":"010"
            },
            "SLLI":{
                "funct3":"001"
            },

            


        }
        self.B_type = {
            "BEQ": {
                "funct3": "000"
            },
            "BNE": {
                "funct3": "001"
            },
            "BLT": {
                "funct3": "100"
            },
            "BLTU": {
                "funct3": "110"
            },
            "BGE": {
                "funct3": "101"
            },
            "BGEU": {
                "funct3": "101"
            }
        }
