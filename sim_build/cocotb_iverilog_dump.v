module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/core.fst");
    $dumpvars(0, core);
end
endmodule
