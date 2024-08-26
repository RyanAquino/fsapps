from datetime import datetime

import requests
from bs4 import BeautifulSoup
from loguru import logger
from sqlalchemy.orm import sessionmaker

from models import AAIISentiment, init_db


def scrape_live_data(last_record_date: datetime):
    """
    Scrape live data of aaii.com bearish, bullish, neutral percentages.

    :param last_record_date: last recorded date in database
    :return: records to be saved if any
    """
    website_url = "https://www.aaii.com/sentimentsurvey/sent_results"
    google_cache_url = (
        f"https://webcache.googleusercontent.com/search?q=cache:{website_url}"
    )
    resp = requests.get(google_cache_url)
    html_source = resp.text
    soup = BeautifulSoup(html_source, "html.parser")
    records = soup.findAll("tr", {"align": "center"})[1:-1]
    record_data = []

    for record in records:
        vals = [val.text.strip(" ").replace("%", "") for val in record.findAll("td")]
        report_date, bullish, neutral, bearish = vals
        record_date = datetime.strptime(report_date, "%b %d").replace(
            year=datetime.now().year
        )
        record_item = AAISentiment(
            record_date=str(record_date),
            bullish=bullish,
            neutral=neutral,
            bearish=bearish,
        )

        if last_record_date and last_record_date >= record_date:
            logger.info(
                f"Last recorded date is {last_record_date} - found {record_date}"
            )
            break

        record_data.append(record_item)
        logger.info(f"{record_date} - {bullish} - {neutral} - {bearish}")

    return record_data


def main(session):
    """
    Main job scraper function.

    :param session: sqlalchemy db session
    :return: None
    """
    logger.info("Scraping AAII.com")
    last_record = (
        session.query(AAIISentiment).order_by(AAIISentiment.record_date.desc()).first()
    )
    if last_record:
        last_record = datetime.strptime(last_record.record_date, "%Y-%m-%d %H:%M:%S")

    records_data = scrape_live_data(last_record)

    if records_data:
        session.bulk_save_objects(records_data)
        session.commit()
        logger.success("Done saving new records for aaii.com")
    else:
        logger.info("No records to be save")


if __name__ == "__main__":
    db_engine = init_db()
    Session = sessionmaker(bind=db_engine)
    db_session = Session()
    main(db_session)
