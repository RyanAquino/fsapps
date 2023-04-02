from model import Base
from model import insert
from model import OpCashBal, OpCashDpstWdrl, PubDebtTrans, PubDebtCashAdj
from model import DebtSubjLim, FedTaxDpst, StCashInvest, IncmTaxRfnd

def normalize_table_data(data):
    raw = data.replace("—", " ").replace("–"," ").replace("-","").replace("º","").replace("]","")
    raw_data = ' '.join(raw.split())
    raw_data_list = raw_data.split(" ")
    
    # Handle roman numerals with l
    raw_data_list[1] = raw_data_list[1].replace("l","I")
    
    return raw_data_list[1], " ".join(raw_data_list[2:])

def create_objects(table_info, data):
    objects = []
    exceptions = []

    for i in data:

        try:
            account = list(i.keys())[0]

            if "Operating Cash Balance".startswith(table_info[1]):
                objects.append(
                    OpCashBal(
                        record_date="",
                        account_type=account,
                        close_today_bal=i[account][0],
                        open_today_bal=i[account][1],
                        open_month_bal=i[account][2],
                        open_fiscal_year_bal=i[account][3],
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 1
                    )
                )

            if "Deposits and Withdrawals of Operating Cash".startswith(table_info[1]):
                objects.append(
                    OpCashDpstWdrl(
                        record_date = "",
                        account_type = "",
                        transaction_type = "",
                        transaction_catg = account,
                        transaction_today_amt = i[account][0],
                        transaction_mtd_amt = i[account][1],
                        transaction_fytd_amt = i[account][2],
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 2
                    )
                )

            if "Public Debt Transactions".startswith(table_info[1]):
                objects.append(
                    PubDebtTrans(
                        record_date = "",
                        transaction_type = "",
                        security_market = "",
                        security_type = account,
                        transaction_today_amt = i[account][0],
                        transaction_mtd_amt = i[account][1],
                        transaction_fytd_amt = i[account][2],
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 3
                    )
                )

            if "Adjustment of Public Debt Transactions to Cash Basis".startswith(table_info[1]):
                objects.append(
                    PubDebtCashAdj(
                        record_date = "",
                        transaction_type = "",
                        adj_type = account,
                        adj_today_amt = i[account][0],
                        adj_mtd_amt = i[account][1],
                        adj_fytd_amt = i[account][2],
                        sub_table_name = "",
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 4
                    )
                )
            
            if "Debt Subject to Limit".startswith(table_info[1]):
                objects.append(
                    DebtSubjLim(
                        record_date = "",
                        debt_catg = account,
                        close_today_bal = i[account][0],
                        open_today_bal = i[account][1],
                        open_month_bal = i[account][2],
                        open_fiscal_year_bal = i[account][3],
                        sub_table_name = "",
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 5
                    )
                )

            if "Federal Tax Deposits".startswith(table_info[1]):
                objects.append(
                    FedTaxDpst(
                        record_date = "",
                        tax_deposit_type = account,
                        tax_deposit_today_amt = i[account][0],
                        tax_deposit_mtd_amt = i[account][1],
                        tax_deposit_fytd_amt = i[account][2],
                        sub_table_name = "",
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 6
                    )
                )

            if "Tax and Loan Note Accounts by Depositary Category".startswith(table_info[1]):
                objects.append(
                    StCashInvest(
                        transaction_type = "",
                        transaction_type_desc = account,
                        depositary_type_a_amt = i[account][0],
                        depositary_type_b_amt = i[account][1], 
                        depositary_type_c_amt = i[account][2],
                        total_amt = i[account][3],
                        sub_table_name = "",
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 7
                    )
                )
            if "Short Term Cash Investments".startswith(table_info[1]):
                objects.append(
                    StCashInvest(
                        transaction_type = "",
                        transaction_type_desc = account,
                        depositary_type_a_amt = i[account][0],
                        depositary_type_b_amt = i[account][1], 
                        depositary_type_c_amt = i[account][2],
                        total_amt = i[account][3],
                        sub_table_name = "",
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 8
                    )
                )

            if "Income Tax Refunds Issued".startswith(table_info[1]):
                objects.append(
                    IncmTaxRfnd(
                        record_date = "",
                        tax_refund_type = account,
                        tax_refund_today_amt = i[account][0],
                        tax_refund_mtd_amt = i[account][1],
                        tax_refund_fytd_amt = i[account][2],
                        sub_table_name = "",
                        record_fiscal_year = "",
                        record_fiscal_quarter = "",
                        record_calendar_year = "",
                        record_calendar_quarter = "",
                        record_calendar_month = "",
                        record_calendar_day = "",
                        table_id = 9
                    )
                )
        except IndexError as err:
            exceptions.append({
                "table": table_info,
                "data": i[account],
                "msg": err 
            })
    
    return objects, exceptions

def insert_data(result, source):

    exceptions = []

    for key, val in result.items():
        table_info = normalize_table_data(key)

        objects, exceptions = create_objects(table_info, val)
        insert(objects)
    
    return exceptions