import openpyxl
import pdfplumber
import re
import os


def get_table_coordinate(worksheet):
    first_occurrence = {}
    last_occurrence = {}

    for row in worksheet.iter_rows(min_row=2, min_col=worksheet.min_column, max_col=worksheet.max_column):
        cell = row[0]
        value = cell.value

        if value not in first_occurrence:
            first_occurrence[value] = cell.row
        last_occurrence[value] = cell.row

    return [first_occurrence, last_occurrence]


def parse_excel(file):
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['DTS Report']
    table_mapping = {}
    table_data = {}

    # Get each table coordinates
    coordinates = get_table_coordinate(worksheet)
    table_mapping = {table: worksheet[f"A{row}":f"F{coordinates[1][table]}"]
                     for table, row in coordinates[0].items()}

    # Get cell value for each table
    for table, cell_range in table_mapping.items():
        table_number = table.split("-")[0].strip()
        table_data[table_number] = []
        for row in cell_range:
            table_data[table_number].append([cell.value for cell in row[1:]])

    return table_data


def extract_table_data(pdf):
    for page in pdf.pages:
        try:
            if not page.horizontal_edges:
                continue

            start = min([x['x0'] for x in page.horizontal_edges])
            end = max([x['x1'] for x in page.horizontal_edges])

            table_setting = {
                "vertical_strategy": "lines",
                "explicit_vertical_lines": [start, end],
                "horizontal_strategy": "text",
                "intersection_x_tolerance": 10,
            }

            tables = page.extract_table(table_setting)

            for table in tables:
                yield [i for i in table if i is not None and i != ""]

        except Exception as e:
            print(e)


def section_list(data, search_texts):
    sublists = {}
    current_sublist = []
    current_key = None

    for index, item in enumerate(data):

        if len(item) > 0:
            first_element = item[0].replace("—", "-").replace("–", "-").replace("cont.", "").split("-")[-1].strip()
            found = [first_element == text and "TABLE" in item[0] for text in search_texts]

            if any(found):
                current_key = search_texts[found.index(True)]

                if current_key not in sublists:
                    sublists[current_key] = []

            if current_key is not None:
                sublists[current_key].append(item)

    return sublists


def slice_list(lst):
    # Remove symbol and comma and convert all digit to int in the list
    remove_symbols = lambda x: re.sub(r'^\W+|\W+$', '', str(x.replace(',', '')))
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

    for key, data in data.items():
        mapping[key] = [[], []]

        for idx, item in enumerate(data):
            sliced = slice_list(item)

            if len(sliced) == 1 and len(sliced[0]) > 3:
                mapping[key][0].append(sliced[0])

            if len(sliced) == 2 and len(sliced[1]) > 3:
                mapping[key][0].append(sliced[0])
                mapping[key][1].append(sliced[1])

    return mapping


def parse_pdf(filename):
    with pdfplumber.open(filename) as pdf:
        # Extract all table data
        data = extract_table_data(pdf)

        # Section data
        search_texts = [
            "Operating Cash Balance",
            "Deposits and Withdrawals of Operating Cash",
            "Public Debt Transactions",
            "Adjustment of Public Debt",
            "Adjustment of Public Debt Transactions to Cash Basis",
            "Debt Subject to Limit",
            "Short-Term Cash Investments",
            "Federal Tax Deposits",
            "Tax and Loan Note Accounts",
            "Income Tax Refunds Issued",
            # "Daily Treasury Statement Footnotes:"
        ]
        sectioned_data = section_list(data, search_texts)

        flattened_data = flatten_data(sectioned_data)

        flattened_data["Federal Tax Deposits"][0].append(flattened_data["Income Tax Refunds Issued"].pop(0))
        flattened_data["Tax and Loan Note Accounts"][0].append(flattened_data["Federal Tax Deposits"].pop(1))

        # Flatten data
        for key, val in flattened_data.items():
            print(key, val)


def parse():
    base_path = os.path.join(os.getcwd(), "data")

    for year in os.listdir(base_path)[1:2]:
        year = "1998"
        if os.path.isdir(os.path.join(base_path, year)):
            for file in os.listdir(os.path.join(base_path, year))[0:1]:
                if file.split(".")[-1] == "xlsx":
                    parse_excel(os.path.join(base_path, year, file))

                if file.split(".")[-1] == "pdf":
                    parse_pdf(os.path.join(base_path, year, file))


if __name__ == "__main__":
    parse()
