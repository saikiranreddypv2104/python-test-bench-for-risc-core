module core(clk,reset);
    input clk,reset;
    wire [3:0] ALU_op;
    wire [6:0]funct7;
    wire [2:0]funct3;
    wire [6:0] opcode;
    wire [1:0] ImmSel;
    wire MemRead,MemWrite,ALUsrc,MemtoReg,branch;
    
    datapath       dataPath   (clk,reset,ALU_op,RegWrite,MemRead,MemWrite,ALUsrc,MemtoReg,branch,ImmSel,funct7,funct3,opcode);
    control_path   controlPath     (clk,reset,opcode,funct7,funct3,ALU_op,RegWrite,MemRead,MemWrite,ALUsrc,MemtoReg,ImmSel,branch);
endmodule