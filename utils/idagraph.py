import idc
idc.auto_wait()
filename=idc.ARGV[1]
ida_gdl.gen_simple_call_chart(filename,"gen chart...",'title',ida_gdl.CHART_GEN_GDL)
idc.auto_wait()
qexit(0)
