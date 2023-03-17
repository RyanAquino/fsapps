import re
from pathlib import Path
import pdfplumber


def extract_pdf(pdf):
    table_setting = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "intersection_x_tolerance": 10,
    }

    for page in pdf.pages:
        try:
            if not page.horizontal_edges:
                continue

            start = min([x["x0"] for x in page.horizontal_edges])
            end = max([x["x1"] for x in page.horizontal_edges])
            table_setting["explicit_vertical_lines"] = [start, end]

            tables = page.extract_table(table_setting)

            if not tables:
                print(f"No tables found for file: {pdf.stream.name}")
                continue

            for table in tables:
                yield [i for i in table if i is not None and i != ""]

        except Exception as e:
            print(str(e))

def section_list(data, search_texts):
    sub_lists = {}
    current_key = None

    for index, item in enumerate(data):
        if len(item) > 0:
            first_element = (
                item[0]
                .replace("—", "-")
                .replace("–", "-")
                .replace("cont.", "")
                .split("-")[-1]
                .strip()
            )
            found = [
                first_element == text and "TABLE" in item[0] for text in search_texts
            ]

            if any(found):
                current_key = search_texts[found.index(True)]

                if current_key not in sub_lists:
                    sub_lists[current_key] = []

            if current_key is not None:
                sub_lists[current_key].append(item)

    return sub_lists

def slice_list(lst):
    # Remove symbol and comma and convert all digit to int in the list
    remove_symbols = lambda x: re.sub(r"^\W+|\W+$", "", str(x.replace(",", "")))
    res = []

    for x in lst:
        item = remove_symbols(x)

        if item.isdigit():
            res.append(int(item))
        else:
            if item == "":
                item = 0
            res.append(item)

    # Find all index of the string
    indexes = [i for i, x in enumerate(res) if isinstance(x, str)]

    # Slice the list based on the index of the string
    return [res[i:j] for i, j in zip(indexes, indexes[1:] + [None])]

def flatten_data(data):
    mapping = {}

    for key, val in data.items():
        mapping[key] = [[], []]

        for idx, item in enumerate(val):
            sliced = slice_list(item)

            if len(sliced) == 1 and len(sliced[0]) > 3:
                mapping[key][0].append(sliced[0])

            if len(sliced) == 2 and len(sliced[1]) > 3:
                mapping[key][0].append(sliced[0])
                mapping[key][1].append(sliced[1])

    return mapping

def extract_data(file):

    result = []
    
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            # Extract all words on each page
            raw_words = page.extract_text().split("\n")
                    
            # Remove the $ and . and , symbols
            pattern = r"[$\.,]+"
            data = [re.sub(pattern, "", x) for x in raw_words]
            
            result.extend(data)

    return result

def parse_pdf(filename):
    try:
        data = extract_data(filename)

        print(data)
    
    except Exception as e:
        print(str(e))

    # search_texts = [
    #     "Operating Cash Balance",
    #     "Deposits and Withdrawals of Operating Cash",
    #     "Public Debt Transactions",
    #     "Adjustment of Public Debt",
    #     "Adjustment of Public Debt Transactions to Cash Basis",
    #     "Debt Subject to Limit",
    #     "Short-Term Cash Investments",
    #     "Federal Tax Deposits",
    #     "Tax and Loan Note Accounts",
    #     "Income Tax Refunds Issued",
    # ]
    # try:
    #     with pdfplumber.open(filename) as pdf:
    #         data = extract_data(pdf)


    #         # # Section data
    #         # sectioned_data = section_list(data, search_texts)

    #         # flattened_data = flatten_data(sectioned_data)

    #         # # Special cases
    #         # if tax_deposit := flattened_data.get("Federal Tax Deposits") and (
    #         #         tax_refund := flattened_data.get("Income Tax Refunds Issued")
    #         # ):
    #         #     tax_deposit[0].append(tax_refund.pop(0))

    #         # if tax_loan := flattened_data.get("Tax and Loan Note Accounts") and (
    #         #         tax_deposit := flattened_data.get("Federal Tax Deposits")
    #         # ):
    #         #     tax_loan[0].append(tax_deposit.pop(1))

    #         # print(pdf.stream.name)
    #         # print(sectioned_data)

    # except Exception as e:
    #     logger.error(e)


def parse():
    path = (Path.cwd() / "data").glob("99120*.pdf")
    for file in path:
        parse_pdf(file)


if __name__ == "__main__":
    parse()
