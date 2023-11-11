from vnstock import * #import all functions

symbol = "FPT"
report_range='quarterly'
report_time = "2023-Q3"

def calculate_roic(symbol, report_range, report_time):
    #============ Theo TCBS =============
    print("======TCBS======")
    #Bổ sung param `get_all` để lấy tất cả báo cáo hoặc 5 năm gần nhất hoặc 10 quý gần nhất
    tcbs_income_statement = financial_flow(symbol, report_type='incomestatement', report_range=report_range, get_all=False).T
    tcbs_balance_sheet = financial_flow(symbol, report_type='balancesheet', report_range=report_range, get_all=False).T
    print("Income statement: " + str(tcbs_income_statement))
    print("Balance Sheet: " + str(tcbs_balance_sheet))

    equity = tcbs_balance_sheet.loc["equity"][report_time]
    cash = tcbs_balance_sheet.loc["cash"][report_time]
    debt_total = tcbs_balance_sheet.loc["shortDebt"][report_time]
    post_tax_profit = tcbs_income_statement.loc["postTaxProfit"][report_time]
    roic = round(post_tax_profit / (equity + debt_total - cash), 3)
    print("Post Tax Profit: " + str(post_tax_profit))
    print("Total Debt (Short + Long): " + str(debt_total))
    print("Cash: " + str(cash))
    print("Equity: " + str(equity))
    print("ROIC: " + str(roic*100) + "%")
    return roic
#================== Theo SSI =================
# ssi_income_statement_quarterly = financial_report (symbol=stock, report_type='IncomeStatement', frequency='Quarterly')
# print("====SSI Income Statement Quarterly====")
# print(ssi_income_statement_quarterly.to_string())
# nopat = ssi_income_statement_quarterly.loc[21]["Q3 2023"]/10000000
# ssi_balance_sheet_quarterly = financial_report (symbol=stock, report_type='BalanceSheet', frequency='Quarterly')

# print("====SSI Balance Sheet Quarterly====")
# print(ssi_balance_sheet_quarterly.to_string())
# equity = ssi_balance_sheet_quarterly.loc[35]["Q3 2023"]/10000000
# debt = ssi_balance_sheet_quarterly.loc[27]["Q3 2023"]/10000000
# cash = ssi_balance_sheet_quarterly.loc[1]["Q3 2023"]/10000000
# equity_debt = ssi_balance_sheet_quarterly.loc[26]["Q3 2023"]/10000000
# invested_capital = equity_debt - cash
# print("Lợi nhuận sau thuế: " + str(nopat))
# print("Vốn đầu tư: " + str(invested_capital))
# print("Tiền: " + str(cash))

# ssi_roic = nopat / invested_capital
# print("ROIC: " + str(ssi_roic*100) + "%")


# print("Profit After Tax: " + str(tcbs_income_statement_quarterly.loc["postTaxProfit"]["2023-Q3"]))

tcbs_roic = calculate_roic(symbol, report_range, report_time)
# print("TCBS Balance Sheet Quarterly")
# print(tcbs_balance_sheet_quarterly.to_string())
# print("Debt: " + str(tcbs_balance_sheet_quarterly.loc["debt"]["2023-Q3"] ))
# print("Cash: " + str(tcbs_balance_sheet_quarterly.loc["cash"]["2023-Q3"] ))
# roic = 