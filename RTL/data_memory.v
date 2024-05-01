module data_memory(reset,address,read_data,write_data,MemRead,MemWrite,clk);
    input [31:0] address,write_data;
    input reset;
    output reg [31:0]  read_data;
    input MemRead,MemWrite;
    input clk;
    
    reg [31:0] memory [999:0];
    integer i;
    assign read_data=MemRead? memory[address]:32'dx;
    always @(negedge clk)begin
        if (reset) begin
            for(i=0;i<1000;i=i+1) begin
                memory[i]=i;
            end
            
        end
        else begin
        //if MemRead , if its value is 0 it will give all zeros
        //if its value is 1 then it will give the write data
        //case(MemRead)
        //    1:read_data=memory[address];
         //   0:read_data=32'd0;
        //endcase
        //if MemWrite is zero then previous value will be stores
        case(MemWrite)
            0:memory[address]=memory[address];
            1:memory[address]=write_data;
        endcase
        end
        
    end
    

endmodule