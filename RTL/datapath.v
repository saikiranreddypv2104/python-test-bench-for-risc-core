`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/09/2024 03:35:00 PM
// Design Name: 
// Module Name: datapath
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module datapath(clk,reset,ALU_op,RegWrite,MemRead,MemWrite,ALUsrc,MemtoReg,branch,ImmSel,funct7,funct3,opcode);
    input clk,reset,RegWrite;
    input [3:0] ALU_op;
    output [6:0]funct7;
    output [2:0]funct3;
    output [6:0] opcode;
    input  MemRead,MemWrite,ALUsrc,MemtoReg,branch;
    input [1:0] ImmSel;
  //for pc
     wire [31:0] pc,pc_plus_4,pc_next;
     //decoder
     wire [6:0]funct7;
     wire [2:0]funct3;
     wire [6:0] opcode;
     wire [4:0] rs2,rs1,rd; 
     wire [31:0] imm;
     //instruction memory
     wire [31:0] instruction;
     //register memory
     wire [4:0] read_reg_1,read_reg_2;
     wire [4:0] write_reg;//RegWrite signal
     wire [31:0] data1,data2,write_data ; 
     assign read_reg_1=rs1;
     assign read_reg_2=rs2;
     assign write_reg=rd;  
     //alu control
     wire [31:0] A,B,ALUout;
     //ALU_OP signsl
     assign A=data1;
     assign B=data2;
     //sign extension 
     wire [31:0] extended_imm;
     //mux ALUsrc 
      wire [31:0] ALUsrc_out;
      //data memory
      wire [31:0] read_data;
      wire MemRead,MemWrite;
      wire MemtoReg;
      wire [31:0] extended_imm_shifted;
      wire [31:0] branch_to_pc;
      wire PCSrc,Zero;
      
      assign PCSrc=branch&Zero;
      assign rs1=instruction[19:15];
      assign rs2=instruction[24:20];
      assign rd =instruction[11:7];
      assign funct3=instruction[14:12];
      assign funct7=instruction[31:25];
      assign opcode=instruction[6:0];
      
      Dflop               PC                (clk,pc_next,pc,reset);//reset
      adder               PCadder           (pc, 32'd4, pc_plus_4 );//pc adder block
      instruction_memory  inst_memory       (pc,instruction,reset);
      register_memory     reg_mem           (clk,reset,read_reg_1,read_reg_2,write_reg,write_data,RegWrite,data1,data2);//write_data
      ALU                 alu               (A,ALUsrc_out,ALUout, ALU_op,Zero);
      data_memory         data_Mem      (reset,ALUout,read_data,data2,MemRead,MemWrite,clk);//MemRead,MemWrite
      mux                 ALUsrc_mux        (imm,data2,ALUsrc,ALUsrc_out);//alusr
      mux                 memtoreg_mux      (read_data,ALUout,MemtoReg,write_data);//MemtoReg
      shift_left          shift_left_one    (imm,extended_imm_shifted);
      adder               bracnh_adder      (extended_imm_shifted,pc,branch_to_pc);
      mux                 pc_sel_branch     (branch_to_pc,pc_plus_4,PCSrc,pc_next);//PCSrc
      ImmGen              immediate_gen     (instruction,ImmSel,imm);//ImmSel
  
  
endmodule
