`timescale 1ns / 1ps
module control_path(clk,reset,opcode,funct7,funct3,ALU_op,RegWrite,MemRead,MemWrite,ALUsrc,MemtoReg,ImmSel,branch);
    input clk,reset;
    output  [3:0] ALU_op;
    input [6:0]funct7;
    input [2:0]funct3;
    input [6:0] opcode;
    wire [3:0] ALU_op1;
    reg [1:0] instruction_type;
    output reg RegWrite,MemRead,MemWrite,ALUsrc,MemtoReg,branch;
    output  reg [1:0] ImmSel;
    assign ALU_op=ALU_op1;
    alu_control alu_ctrl (funct7[5],funct3,instruction_type,ALU_op1);
    always @(*)begin
        case(opcode)
            7'b0110011:begin//Rinstruction_type
                $display("Rinstruction_type opcode =%0h ",7'b0110011);
                ImmSel=2'bxx;
                instruction_type=2'b10;
                RegWrite=1;
                ALUsrc=0;
                MemtoReg=0;
                MemRead=0;
                MemWrite=0;
                branch=0;
            end
            7'b0010011:begin//immediate #Todo
                $display("immediate instruction_type");
                ImmSel=2'b00;
                instruction_type=2'b11;
                RegWrite=1'b1;
                ALUsrc=1'b1;
                MemtoReg=1'b0;
                MemRead=1'b0;
                MemWrite=1'b0;
                branch=0;
            end
            7'b0000011:begin//load
                $display("load");
                ImmSel=2'b00;
                instruction_type=2'b00;
                RegWrite=1'b1;
                ALUsrc=1'b1;
                MemtoReg=1'b1;
                MemRead=1'b1;
                MemWrite=1'b0;
                branch=0;            end
            7'b0100011:begin//store S
                $display("strore s");
                ImmSel=2'b01;
                instruction_type=2'b00;
                RegWrite=1'b0;
                ALUsrc=1'b1;
                MemtoReg=1'b0;
                MemRead=1'b0;
                MemWrite=1'b1;
                branch=0;
            end
            7'b1100011:begin//Sequence Branch
                $display("sequence branch");
                ImmSel=2'b10;
                instruction_type=2'b01;
                RegWrite=1'b0;
                ALUsrc=1'b0;
                MemtoReg=1'b0;
                MemRead=1'b0;
                MemWrite=1'b0;
                branch=1;
            end
            default:begin
                $display("default case is invoked");
                $display("Opcode is %0h",opcode);
                $display("time =%0t",$time);
                ImmSel=2'b00;
                instruction_type=2'b00;
                RegWrite=1'b0;
                ALUsrc=1'b0;
                MemtoReg=1'b0;
                MemRead=1'b0;
                MemWrite=1'b0;
                branch=0;
            
            end
        endcase//opcode case
        
    end
    
endmodule
