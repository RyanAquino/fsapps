import re
from datetime import datetime
from itertools import chain

from model import insert
from model import OpCashBal, OpCashDpstWdrl, PubDebtTrans, PubDebtCashAdj
from model import DebtSubjLim, FedTaxDpst, StCashInvest, IncmTaxRfnd


def normalize_table_data(data):
    raw = (
        data.replace("—", " ")
        .replace("–", " ")
        .replace("-", "")
        .replace("º", "")
        .replace("]", "")
    )
    raw_data = " ".join(raw.split())
    raw_data_list = raw_data.split(" ")

    # Handle roman numerals with l
    raw_data_list[1] = raw_data_list[1].replace("l", "I")

    return raw_data_list[1], " ".join(raw_data_list[2:])


def handle_text_parser_special_case(account, i):
    new_data = None
    is_valid = []

    for key in list(i.keys())[1:]:
        is_divided = len(key) == 2
        is_divided_twice = len(key) == 4
        if (is_divided and re.findall(r"^\d\/", key)) or (
            is_divided_twice and re.findall(r"\d/\d/", key)
        ):
            is_valid.append(True)
        else:
            is_valid.append(False)

    if all(is_valid):
        new_data = {account: list(chain(*i.values()))}

    return new_data


def compute_quarter(file_month):
    quarter_mapping = {
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 3,
        10: 4,
        11: 4,
        12: 4,
    }

    return quarter_mapping.get(file_month)


def create_objects(table_info, data, source):
    objects = []
    exceptions = []
    file_date = datetime.strptime(source.stem[:6], "%y%m%d")
    file_year, file_month, file_day = file_date.year, file_date.month, file_date.day
    file_date = file_date.strftime("%Y-%m-%d")
    file_quarter = compute_quarter(file_month)

    for i in data:
        account = list(i.keys())[0]

        if len(i.keys()) > 1:
            print(source)
            print("DEBUG more than 1 key: ", i)

        # Text files special cases e.g 2/ and 2/4/ only
        if len(i.keys()) != 1 and source.suffix == ".txt":
            new_data = handle_text_parser_special_case(account, i)
            if new_data:
                i = new_data
                print("NEW DATA: ", i)

        # Skip unfiltered non-related values
        if len(list(chain(*i.values()))) < 3 or len(i.keys()) > 1:
            print("SKIPPING: ", i)
            continue

        try:
            if "Operating Cash Balance".startswith(table_info[1]):
                close_today = open_today = open_month = open_year = None

                if len(i[account]) == 3:
                    close_today, open_today, open_month = i[account]

                if len(i[account]) == 4:
                    close_today, open_today, open_month, open_year = i[account]

                objects.append(
                    OpCashBal(
                        record_date=file_date,
                        account_type=account,
                        close_today_bal=close_today,
                        open_today_bal=open_today,
                        open_month_bal=open_month,
                        open_fiscal_year_bal=open_year,
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=1,
                    )
                )

            if "Deposits and Withdrawals of Operating Cash".startswith(table_info[1]):
                objects.append(
                    OpCashDpstWdrl(
                        record_date=file_date,
                        account_type="",
                        transaction_type="",
                        transaction_catg=account,
                        transaction_today_amt=i[account][0],
                        transaction_mtd_amt=i[account][1],
                        transaction_fytd_amt=i[account][2],
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=2,
                    )
                )

            if "Public Debt Transactions".startswith(table_info[1]):
                objects.append(
                    PubDebtTrans(
                        record_date=file_date,
                        transaction_type="",
                        security_market="",
                        security_type=account,
                        transaction_today_amt=i[account][0],
                        transaction_mtd_amt=i[account][1],
                        transaction_fytd_amt=i[account][2],
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=3,
                    )
                )

            if "Adjustment of Public Debt Transactions to Cash Basis".startswith(
                table_info[1]
            ):
                objects.append(
                    PubDebtCashAdj(
                        record_date=file_date,
                        transaction_type="",
                        adj_type=account,
                        adj_today_amt=i[account][0],
                        adj_mtd_amt=i[account][1],
                        adj_fytd_amt=i[account][2],
                        sub_table_name="",
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=4,
                    )
                )

            if "Debt Subject to Limit".startswith(table_info[1]):
                close_today = open_today = open_month = open_year = None

                if len(i[account]) == 3:
                    close_today, open_today, open_month = i[account]

                if len(i[account]) == 4:
                    close_today, open_today, open_month, open_year = i[account]

                objects.append(
                    DebtSubjLim(
                        record_date=file_date,
                        debt_catg=account,
                        close_today_bal=close_today,
                        open_today_bal=open_today,
                        open_month_bal=open_month,
                        open_fiscal_year_bal=open_year,
                        sub_table_name="",
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=5,
                    )
                )

            if "Federal Tax Deposits".startswith(table_info[1]):
                objects.append(
                    FedTaxDpst(
                        record_date=file_date,
                        tax_deposit_type=account,
                        tax_deposit_today_amt=i[account][0],
                        tax_deposit_mtd_amt=i[account][1],
                        tax_deposit_fytd_amt=i[account][2],
                        sub_table_name="",
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=6,
                    )
                )

            if "Tax and Loan Note Accounts by Depositary Category".startswith(
                table_info[1]
            ):
                objects.append(
                    StCashInvest(
                        record_date=file_date,
                        transaction_type="",
                        transaction_type_desc=account,
                        depositary_type_a_amt=i[account][0],
                        depositary_type_b_amt=i[account][1],
                        depositary_type_c_amt=i[account][2],
                        total_amt=i[account][3],
                        sub_table_name="",
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=7,
                    )
                )
            if "Short Term Cash Investments".startswith(table_info[1]):
                objects.append(
                    StCashInvest(
                        record_date=file_date,
                        transaction_type="",
                        transaction_type_desc=account,
                        depositary_type_a_amt=i[account][0],
                        depositary_type_b_amt=i[account][1],
                        depositary_type_c_amt=i[account][2],
                        total_amt=i[account][3],
                        sub_table_name="",
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=8,
                    )
                )

            if "Income Tax Refunds Issued".startswith(table_info[1]):
                objects.append(
                    IncmTaxRfnd(
                        record_date=file_date,
                        tax_refund_type=account,
                        tax_refund_today_amt=i[account][0],
                        tax_refund_mtd_amt=i[account][1],
                        tax_refund_fytd_amt=i[account][2],
                        sub_table_name="",
                        record_fiscal_year="",
                        record_fiscal_quarter="",
                        record_calendar_year=file_year,
                        record_calendar_quarter=file_quarter,
                        record_calendar_month=file_month,
                        record_calendar_day=file_day,
                        table_id=9,
                    )
                )
        except IndexError:
            print({"table": table_info, "data": i[account], "file": source.name})
            exceptions.append(
                {"table": table_info, "data": i[account], "file": source.name}
            )

    return objects, exceptions


def insert_data(result, source):
    exceptions = []

    for key, val in result.items():
        table_info = normalize_table_data(key)

        objects, exceptions = create_objects(table_info, val, source)
        insert(objects)

    return exceptions
