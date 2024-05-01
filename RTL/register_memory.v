`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: Bits pilani
// Engineer: sai kiran reddy
// 
// Create Date: 04/09/2024 02:58:04 PM
// Design Name: RISV single cycle
// Module Name: register_memory
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


module register_memory(clk,reset,read_reg_1,read_reg_2,write_reg,write_data,RegWrite,data1,data2);
    input [4:0] read_reg_1,read_reg_2,write_reg;
    input [31:0] write_data;
    output [31:0] data1,data2;
    
    input clk,RegWrite,reset;
    reg [31:0] memory [31:0];
    
    assign data1=memory[read_reg_1];
    assign data2=memory[read_reg_2];
    
    integer i;
    always @(negedge clk) begin
        memory[0]=0;//in riscv register 0 is fixed to zero
        if (reset) begin
            for(i=1;i<32;i=i+1) begin
                memory[i]<=i;
            end
        end
        else if(RegWrite) begin
            memory[write_reg]=write_data;
        end
    end
    
    
endmodule
