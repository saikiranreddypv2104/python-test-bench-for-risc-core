`timescale 1ns / 1ps
module alu_control(funct7,funct3,instruction_type,ALU_op);
    input funct7;
    input [2:0] funct3;
    input [1:0] instruction_type;
    output reg [3:0] ALU_op;
    always @(*) begin
            case(instruction_type)
                2'b00:begin//lw and sw
                    ALU_op=4'b0000;//add
                end
                
                2'b01:begin//Bew
                    ALU_op=4'b1000;//sub
                end
     ///////////////////////////
     //           0010    A+B  //ADD
     //           0000    A&B  //
     //           0001    A|B  //
     //           0111    A^B  //
     //           1111    A<B  //
     //           0001    A<<B //
     //           0110    A-B  //
     ///////////////////////////
                2'b10:begin//Rinstruction_type
                    case({funct7,funct3})
                        4'b0000:ALU_op=4'b0000;//add
                        4'b1000:ALU_op=4'b1000;//sub
                        4'b0111:ALU_op=4'b0111;//and
                        4'b0110:ALU_op=4'b0110;//or
                        4'b0100:ALU_op=4'b0100;//Xor
                        4'b0001:ALU_op=4'b0001;//sll
                        4'b0010:ALU_op=4'b0010;//slt
                        default:ALU_op=4'b0000;//add
                    endcase
                end
                
                2'b11:begin//Iinstruction_type
                    case(funct3)
                        3'b000:ALU_op=4'b0000;//add
                        3'b111:ALU_op=4'b0111;//and
                        3'b110:ALU_op=4'b0110;//or
                        3'b100:ALU_op=4'b0100;//Xor
                        3'b001:ALU_op=4'b0001;//sll
                        3'b010:ALU_op=4'b0010;//slt
                        default:ALU_op=4'b0000;//add
                    endcase       
                end
            endcase
    end
endmodule
