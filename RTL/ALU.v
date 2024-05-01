`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/09/2024 02:31:27 PM
// Design Name: 
// Module Name: ALU
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


module ALU(A,B,out, ALU_op,Zero);
        input [31:0] A;
        input [31:0] B;
        input [3:0] ALU_op;
        output reg [31:0] out;
        output Zero;
        assign Zero=(out==32'd0);

        always @(*) begin
            case(ALU_op)
                4'b0000:out=A+B;//ADD
                4'b0111:out=A&B;//And
                4'b0110:out=A|B;
                4'b0100:out=A^B;
                4'b0010:out=A<B;
                4'b0001:out=A<<B;
                4'b1000:out=A-B;
                default:out=A+B;//by default the result will addition
                                //in case of uncertainity
            endcase
        end
endmodule
