CWD=$(shell pwd)
COCOTB_REDUCED_LOG_FMT = False
SIM ?= icarus
WAVES=1
VERILOG_INCLUDE_DIRS=$(CWD)/RTL
VERILOG_SOURCES=$(CWD)/RTL/adder.v\
		$(CWD)/RTL/Dflop.v\
		$(CWD)/RTL/register_memory.v\
		$(CWD)/RTL/sign_extend.v\
		$(CWD)/RTL/shift_left.v\
		$(CWD)/RTL/mux.v\
		$(CWD)/RTL/ALU.v\
		$(CWD)/RTL/alu_control.v\
		$(CWD)/RTL/core.v\
		$(CWD)/RTL/control_path.v\
		$(CWD)/RTL/data_memory.v\
		$(CWD)/RTL/datapath.v\
		$(CWD)/RTL/ImmGen.v\
		$(CWD)/RTL/instruction_memory.v
MODULE := testBench
TOPLEVEL := core
TOPLEVEL_LANG := verilog
COCOTB_HDL_TIMEUNIT=1us
COCOTB_HDL_TIMEPRECISION=1ns
include $(shell cocotb-config --makefiles)/Makefile.sim
# include ../cleanall.mk
