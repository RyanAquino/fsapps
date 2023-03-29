import re
from pathlib import Path
from fsapps.fsapps.text_parser import format_data, is_day, table_v_data_handler
import wordninja

import pdfplumber


def page_handler(page, coords):
    table_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "intersection_x_tolerance": 10,
    }
    page = page.crop(coords)

    start = min([x["x0"] for x in page.horizontal_edges])
    end = max([x["x1"] for x in page.horizontal_edges])
    table_settings["explicit_vertical_lines"] = [start, end]
    table_data = page.extract_table(table_settings=table_settings)

    if not table_data:
        table_settings["vertical_strategy"] = "lines"
        table_data = page.extract_table(table_settings)

        if table_data:
            table_data = [" ".join(item) for item in table_data if all(item)]
            table_data.insert(0, "TABLE I—Operating Cash Balance")

    return table_data


def flatten_data(pdf_data):
    flatten_fn = lambda l: sum(map(flatten_fn, l), []) if isinstance(l, list) else [l]
    flat_data = flatten_fn(pdf_data)
    filtered_flat_data = []

    for item in flat_data:
        if "TABLE" in item:
            filtered_flat_data.append(item)
            continue

        if item is not None and item != "":
            item = re.sub(r"[\$,]", "", item)
            item = item.replace(".", "").strip()
            item = wordninja.split(item)
            item = " ".join(item)
            filtered_flat_data.append(item)

    return filtered_flat_data


def pdf_parser(file):
    no_edges = []
    pdf_data = []

    with pdfplumber.open(file) as pdf:
        print("Processing: ", pdf.stream.name)

        for page in pdf.pages:
            if not page.horizontal_edges:
                print("WARNING! no horizontal edge: ", pdf.stream.name)
                no_edges.append(pdf.stream.name)
                continue

            if page.page_number == 1:
                # T1
                left = 0
                bottom = page.height * 0.12
                right = page.width
                top = page.height * 0.28
                t1_coords = (left, bottom, right, top)

                # T2
                left = 0
                bottom = page.height * 0.28
                right = page.width
                top = page.height
                t2_coords = (left, bottom, right, top)

                table_1_data = page_handler(page, t1_coords)
                table_2_data = page_handler(page, t2_coords)

                if table_1_data:
                    pdf_data += table_1_data

                if table_2_data:
                    pdf_data += table_2_data

            if page.page_number == 2:
                # Left coordinates
                left = page.width * 0.50
                bottom = 0
                right = page.width
                top = page.height
                right_coords = (left, bottom, right, top)

                # Right coordinates
                left = 0
                bottom = 0
                right = page.width * 0.50
                top = page.height
                left_coords = (left, bottom, right, top)

                left_data = page_handler(page, left_coords)
                right_data = page_handler(page, right_coords)

                if left_data:
                    left_data.insert(0, ["TABLE III-A—Public Debt Transactions"])
                    pdf_data += left_data

                if right_data:
                    right_data.insert(0, ["TABLE III-A—Public Debt Transactions"])
                    pdf_data += right_data

    return pdf_data, no_edges


def transform_data(pdf_data):
    tbl_idx = 0
    mapping = {}
    tbl_key = None

    new_table_v_idx = 1
    is_table_v_new = False

    flatten_pdf_data = flatten_data(pdf_data)
    table_3_ctr = 0

    table_format = [
        ["TABLE I—Operating Cash Balance", "TABLE l—Operating Cash Balance", "TABLE I - Operating Cash Balance"],
        ["TABLE II—Deposits and Withdrawals of Operating Cash", "TABLE ll—Deposits and Withdrawals of Operating Cash",
         "TABLE II - Deposits and Withdrawals of Operating Cash"],
        ["TABLE III-A—Public Debt Transactions", "TABLE III-A—Public Debt Transactions"],
        ["TABLE III-B—Adjustment of Public Debt", "TABLE III-B–Adjustment of Public Debt",
         "TABLE III-B - Adjustment of Public Debt"],
        ["TABLE IV—Federal Tax Deposits", "TABLE IV–Federal Tax Deposits", "TABLE IV - Federal Tax Deposits"],
        ["TABLE III-C—Debt Subject to Limit", "TABLE III-C–Debt Subject to Limit",
         "TABLE III-C - Debt Subject to Limit"],
        ["TABLE V—Tax and Loan Note Accounts", "TABLE V–Tax and Loan Note Accounts",
         "TABLE V - Short-Term Cash Investments"],
        ["TABLE VI—Income Tax Refunds Issued", "TABLE VI–Income Tax Refunds Issued",
         "TABLE VI - Income Tax Refunds Issued"],
    ]

    for pdf_line_data in flatten_pdf_data:
        if is_day(pdf_line_data):
            continue

        if tbl_idx < len(table_format) and pdf_line_data in table_format[tbl_idx]:
            tbl_key = pdf_line_data

            # Special case for split table 3a
            if pdf_line_data in mapping:
                table_3_ctr += 1
                continue

            mapping[tbl_key] = []
            tbl_idx += 1

        processed = format_data(pdf_line_data)

        if processed and tbl_key:
            processed = dict(processed)
            processed, new_table_v_idx = table_v_data_handler(processed, is_table_v_new, new_table_v_idx)

            if len(processed) > 1:
                mapping[tbl_key] += [{k: v} for k, v in processed.items()]
            else:
                # Special case for split table 3a
                if table_3_ctr == 1:
                    tbl_key = "TABLE III-A—Public Debt Transactions"
                    table_3_ctr = 0
                mapping[tbl_key].append(processed)

    return mapping


def main():
    files_path = (Path.cwd().parent / "data").glob("*.pdf")
    no_edges = []
    exceptions = []

    for item in list(files_path):
        try:
            pdf_data, edges = pdf_parser(item)
            no_edges += edges
        except Exception as e:
            exceptions.append({"item": item, "exc": str(e)})
        finally:
            print(transform_data(pdf_data))

    print("No edges: ", no_edges)
    print("Exceptions: ", exceptions)


if __name__ == "__main__":
    main()
