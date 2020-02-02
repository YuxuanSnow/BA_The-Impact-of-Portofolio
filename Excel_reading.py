import xlrd

fund_flow = xlrd.open_workbook('fund_flow_lux.xlsx')
fund_return = xlrd.open_workbook('fund_return_lux.xlsx')
fund_size = xlrd.open_workbook('fund_size_luxembourg20200108.xlsx')
fund_snapshot = xlrd.open_workbook('fund_snapshot_lux.xlsx')
fund_sustainability = xlrd.open_workbook('fund_sustainability_lux.xlsx')

table_flow = fund_flow.sheets()[0]
table_return = fund_return.sheets()[0]
table_size = fund_size.sheets()[0]
table_snapshot = fund_snapshot.sheets()[0]
table_sustainability = fund_sustainability.sheets()[0]

flow_FundId = table_flow.col_values(0)
flow_FundCode = table_flow.col_values(1)
flow_FundLegalName = table_flow.col_values(2)
flow_Name = table_flow.col_values(3)
flow_BaseCurrency = table_flow.col_values(4)
flow_ISIN = table_flow.col_values(5)
flow_Domicile = table_flow.col_values(6)
flow_1 = table_flow.col_values(7)
flow_2 = table_flow.col_values(8)
flow_3 = table_flow.col_values(9)
flow_4 = table_flow.col_values(10)
flow_5 = table_flow.col_values(11)
flow_6 = table_flow.col_values(12)
flow_7 = table_flow.col_values(13)
flow_8 = table_flow.col_values(14)
flow_9 = table_flow.col_values(15)
flow_10 = table_flow.col_values(16)
flow_11 = table_flow.col_values(17)
flow_12 = table_flow.col_values(18)

