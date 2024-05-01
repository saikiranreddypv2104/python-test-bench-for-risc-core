module instruction_memory(PC,Instruction,reset);
    input [31:0] PC;
    input reset;
    output reg [31:0] Instruction;
    reg [31:0] memory [5999:0];

    integer i;
    always@(*) begin
        Instruction = memory[PC];
        //$display("pc=%0d  isntruction=%0h time =%0t",PC,Instruction,$time);
    end
    
    initial begin
        $readmemh("RTL/instruction.mem", memory);
    end
endmodule