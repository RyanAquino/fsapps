from datetime import datetime, timezone, timedelta

import requests
from loguru import logger
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker

from models import init_db, SPYFinance


def scrape_live_data(last_record_dt: datetime):
    """
    Scrape live data of yahoo finance (SPY)

    :param last_record_dt: last recorded date in database
    :return: records to be saved if any
    """
    if not last_record_dt:
        last_record_dt = datetime(1993, 1, 1, 0, 0, tzinfo=timezone.utc)

    current_date = (
        (datetime.now(timezone.utc) + timedelta(days=1))
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .timestamp()
    )
    query_params = {
        "period1": int(last_record_dt.timestamp() + 1),
        "period2": int(current_date),
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(
            "https://finance.yahoo.com/quote/SPY/history/",
            params=query_params,
            headers=headers,
        )
        html_source = response.text
    except requests.exceptions.RequestException:
        logger.warning("Exception raised when sending HTTP requests")
        return []

    soup = BeautifulSoup(html_source, "html.parser")

    table_data = soup.find("div", {"data-testid": "history-table"})

    if not table_data:
        return []

    table_data = table_data.find("div", class_="table-container")
    table_data = table_data.table.tbody
    results = []

    for td in table_data.findAll("tr"):
        dt, *vals = [item.text.strip(" ") for item in td if item and item != " "]
        open_price, high, low, close, adj_close, volume = [
            float(v.replace(",", "")) for v in vals
        ]
        dt = datetime.strptime(dt, "%b %d, %Y")

        if dt.replace(tzinfo=timezone.utc) <= last_record_dt:
            break

        results.append(
            SPYFinance(
                record_date=dt,
                open=open_price,
                high=high,
                low=low,
                close=close,
                adj_close=adj_close,
                volume=volume,
            )
        )

    return results


def main(session):
    """
    Main job scraper function.

    :param session: sqlalchemy db session
    :return: None
    """
    logger.info("Scraping Yahoo finance (SPY)")
    last_record_dt = (
        session.query(SPYFinance).order_by(SPYFinance.record_date.desc()).first()
    )
    if last_record_dt:
        last_record_dt = last_record_dt.record_date.replace(tzinfo=timezone.utc)

    records_data = scrape_live_data(last_record_dt)

    if records_data:
        session.bulk_save_objects(records_data)
        session.commit()
        logger.success("Done saving new records for Yahoo finance (SPY)")
    else:
        logger.info("No records to be save")


if __name__ == "__main__":
    db_engine = init_db()
    Session = sessionmaker(bind=db_engine)
    db_session = Session()
    main(db_session)
