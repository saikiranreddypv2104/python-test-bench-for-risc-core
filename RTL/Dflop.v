`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/09/2024 02:31:27 PM
// Design Name: 
// Module Name: Dflop
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


module Dflop(clk,in,out,reset);
        input [31:0] in;
        output reg [31:0] out;
        input reset;
        input clk;
        always @(posedge clk,posedge reset) begin
            if(reset==1)begin //if reset it high
                out<=32'd0;   // out is assigned to zero
            end
            else begin  //elsr the out is updated to input
                out<=in;
            end
        end
endmodule
