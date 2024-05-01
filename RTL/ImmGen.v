`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/10/2024 03:37:13 PM
// Design Name: 
// Module Name: ImmGen
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


module ImmGen(instruction,ImmSel,imm);
    input [31:0] instruction;
    input [1:0] ImmSel;
    output reg [31:0] imm;
    
    always @(*)begin
        
        case(ImmSel)
            2'b00:begin
                imm={{20{instruction[31]}},instruction[31:20]};
            end//immediate type
            2'b01:begin
                imm={{20{instruction[31]}},instruction[31:25],instruction[11:7]};
            end//store type
            2'b10:begin
                imm={{20{instruction[31]}},instruction[7],instruction[30:25],instruction[11:8]};//s branch type
            end//Sequence Branch
        endcase
    
    end
    
endmodule
