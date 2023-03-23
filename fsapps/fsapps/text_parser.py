import re
from copy import deepcopy

import requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def format_data(line):
    formatted = defaultdict(list)
    label = ""
    i = 0

    line = re.sub(r"[\$,]", "", line)
    line = [i.strip() for i in line.split(" ") if i and i != ""]

    while i < len(line):
        if line[i].lstrip("-").isdigit() and label.strip(" ") != "" and line[i] != '³':
            formatted[label.strip(" ")].append(int(line[i]))
            ctr = 1
            while i + ctr < len(line) and line[i + ctr].lstrip("-").isdigit():
                formatted[label.strip(" ")].append(int(line[i + ctr]))
                ctr += 1
            i += ctr
            i -= 1
            label = ""
        else:
            label += f" {line[i]}"

        i += 1
    return formatted


def is_day(line):
    inp = line.split(" ")[0]
    inp = re.sub(r"\W+", " ", inp).strip()

    try:
        datetime.strptime(inp, "%A")
        return True
    except ValueError:
        return False


def is_table(line, tbl_idx):
    old_format = [
        ["TABLE I  Operating Cash Balance"],
        ["TABLE II     Deposits and Withdrawals of Operating Cash"],
        [
            "TABLE III-A  Public Debt Transactions",
            "TABLE IIIA   Public Debt Transactions",
        ],
        [
            "TABLE III-B  Adjustment of Public Debt Transactions to Cash Basis",
            "TABLE IIIB1  Adjustment of Public Debt Transactions to Cash Basis",
        ],
        ["TABLE IIIB2  Adjustment of Public Debt Transactions to Cash Basis"],
        ["TABLE III-C  Debt Subject to Limit", "TABLE IIIC  Debt Subject to Limit"],
        ["TABLE IV     Federal Tax Deposits", "TABLE IV Inter-agency Tax Transfers"],
        [
            "TABLE V      Tax and Loan Note Accounts by Depositary Category",
            "TABLE V  Short-Term Cash Investments",
            "TABLE V  Income Tax Refunds Issued",
        ],
        [
            "TABLE VI     Income Tax Refunds Issued",
            "TABLE VI  Income Tax Refunds Issued",
        ],
    ]
    vals = []

    for words in old_format[tbl_idx]:
        vals = []
        for word in list(filter(lambda x: x != "", words.split(" "))):
            if word not in list(filter(lambda x: x != "", line.split(" "))):
                vals.append(False)
            else:
                vals.append(True)
        if all(vals):
            break

    return all(vals)


def text_parser(data):
    mapping = {}
    tbl_idx = 0
    table_name = ""
    parsed_tables = []

    is_table_v_new = False
    new_table_v_idx = 0

    for i, line in enumerate(data.split("\n")):
        line = line.strip()

        if "TABLE" in line and is_table(line, tbl_idx):
            # print(f"TABLE: {line.strip().replace('³', '')}")

            # Remove unecessary characters
            table_name = line.replace("|", "").replace("³", "")

            # Replace multiple space with a single space
            table_name = ' '.join(table_name.split())

            mapping[table_name] = []
            parsed_tables.append(table_name)
            if parsed_tables and "III-B" in parsed_tables[-1]:
                tbl_idx += 1
            tbl_idx += 1
            continue

        if "PAGE" in line or (line.split(" ") and is_day(line)):
            continue

        processed = format_data(line)
        if processed:

            # Determine if table V new format
            if 'Short-Term Cash Investments (Table V)' in processed:
                is_table_v_new = True

            processed, new_table_v_idx = table_v_data_handler(processed, is_table_v_new, new_table_v_idx)
            mapping[table_name].append(dict(processed))

    return mapping


def table_v_data_handler(processed, is_table_v_new, new_table_v_idx):
    table_v_mappings = [
        "Tax and Loan Note Accounts",
        "Transfers from Federal Reserve Account",
        "Total Tax and Loan Note",
        "Transfers to Federal Reserve Account"
    ]
    processed = deepcopy(processed)

    for key, item in list(processed.items()):
        if key == "(Table V)" or key == "Table V":
            if is_table_v_new:
                new_table_v_idx += 1
                processed[f"{table_v_mappings[new_table_v_idx]} {key}"] = processed.pop(key)
            else:
                processed[f"{table_v_mappings[new_table_v_idx]} {key}"] = processed.pop(key)

            new_table_v_idx += 1

        if (key == "Accounts (Table V)" or key == "Accounts Table V") and not is_table_v_new:
            processed[f"{table_v_mappings[new_table_v_idx]} {key}"] = processed.pop(key)
            new_table_v_idx += 1

    return processed, new_table_v_idx


def main():
    files_path = (Path.cwd().parent / "data").glob("*.txt")
    files_with_exception = []

    for item in list(files_path)[0:10]:
        print(f"Processing: {item.name}")

        try:
            with open(item) as f:
                data = f.read()
                result = text_parser(data)

        except UnicodeDecodeError:
            # Handle corrupted text files
            url = f"https://fsapps.fiscal.treasury.gov/dts/files/{item.name}"
            print(f"Sending request to : {url}")
            response = requests.get(url)
            data = response.text
            files_with_exception.append(item.name)
            result = text_parser(data)
        finally:
            for key, val in result.items():
                print(key)
                for i in val:
                    print(i)

    print(files_with_exception, len(files_with_exception))


if __name__ == "__main__":
    main()
