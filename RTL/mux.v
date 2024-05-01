`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/09/2024 02:31:27 PM
// Design Name: 
// Module Name: mux
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


module mux(A,B,sel,out);
    input [31:0] A;
        input [31:0] B;
        input sel;
        output [31:0] out;
        
        assign out=sel?A:B;
        //out==A when sel==1
        //out==B when sel==0
        
endmodule
