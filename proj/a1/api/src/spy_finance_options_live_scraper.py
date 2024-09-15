from datetime import datetime, timezone
import random
from typing import Callable

import time
import requests
import schedule
import sqlalchemy
from loguru import logger
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker

from models import init_db, SPYFinanceOptions


def send_page_request(ts: int = None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    }
    query_params = {}

    if ts:
        query_params["date"] = ts

    try:
        response = requests.get(
            "https://finance.yahoo.com/quote/%5ESPX/options/",
            headers=headers,
            params=query_params,
        )
        html_source = response.text
    except requests.exceptions.RequestException:
        logger.warning("Exception raised when sending HTTP requests")
        return []

    return html_source


def send_api_request(ts: int = None):
    params = {
        "formatted": True,
        "straddle": False,
        "en": "US",
        "region": "US"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Accept-Encoding": "gzip, deflate, br, zstd",
        # "Accept-Language": "en-US,en;q=0.9",
        # "Cache-Control": "max-age=0",
    }

    if ts:
        params["date"] = ts

    try:
        response = requests.get("https://query1.finance.yahoo.com/v6/finance/options/%5ESPX", params=params, headers=headers)
        response_data = response.json()
        return response_data.get("optionChain", {}).get("result")[0]
    except requests.exceptions.RequestException as e:
        logger.warning(f"Exception raised when sending HTTP requests: {str(e)}")
        return None


def scrape_live_data(session):
    """
    Scrape live data of yahoo finance (SPY)

    :return: records to be saved if any
    """
    response = send_api_request()
    opts = response.get("expirationDates")

    for opt in opts:
        raw_dt = datetime.fromtimestamp(opt, timezone.utc)
        response = send_api_request(opt)
        idx_opt = response.get("options")[0]
        results = []

        for item in idx_opt.get("calls"):
            results.append(
                SPYFinanceOptions(
                    contract_name=item.get("contractSymbol"),
                    last_trade_date=datetime.fromtimestamp(item.get("lastTradeDate").get("raw"), timezone.utc),
                    strike=item.get("strike").get("raw"),
                    last_price=item.get("lastPrice").get("raw"),
                    bid=item.get("bid").get("raw"),
                    ask=item.get("ask").get("raw"),
                    change=item.get("change").get("raw"),
                    change_percent=item.get("percentChange").get("raw"),
                    volume=item.get("volume", {}).get("raw", 0),
                    open_interest=item.get("openInterest").get("raw"),
                    implied_volatility=item.get("impliedVolatility").get("raw"),
                    calls=True,
                    in_the_money=item.get("inTheMoney"),
                )
            )

        for item in idx_opt.get("puts"):
            results.append(
                SPYFinanceOptions(
                    contract_name=item.get("contractSymbol"),
                    last_trade_date=datetime.fromtimestamp(item.get("lastTradeDate").get("raw"), timezone.utc),
                    strike=item.get("strike").get("raw"),
                    last_price=item.get("lastPrice").get("raw"),
                    bid=item.get("bid").get("raw"),
                    ask=item.get("ask").get("raw"),
                    change=item.get("change").get("raw"),
                    change_percent=item.get("percentChange").get("raw"),
                    volume=item.get("volume", {}).get("raw", 0),
                    open_interest=item.get("openInterest").get("raw"),
                    implied_volatility=item.get("impliedVolatility").get("raw"),
                    calls=False,
                    in_the_money=item.get("inTheMoney"),
                )
            )

        if results:
            session.bulk_save_objects(results)
            session.commit()
            logger.success("Done saving new records for Yahoo finance (SPY) Options")
        else:
            logger.info(f"No records to be save - {raw_dt}")


        # html_source = send_page_request(int(opt))
        #
        # if not html_source:
        #     continue
        #
        # soup = BeautifulSoup(html_source, "html.parser")
        #
        # table_data = soup.find("section", {"data-testid": "options-list-table"})
        #
        # if not table_data:
        #     continue
        #
        # tables_data = table_data.findAll("div", class_="tableContainer")
        # results = []
        # calls = True
        #
        # for td in tables_data:
        #     for row in td.table.findAll("tr")[1:]:
        #         vals = [item.text.strip(" ") for item in row if item and item != " "]
        #
        #         if len(vals) == 1:
        #             break
        #
        #         (
        #             contract_name,
        #             dt,
        #             strike,
        #             last_price,
        #             bid,
        #             ask,
        #             change,
        #             change_percent,
        #             volume,
        #             open_interest,
        #             implied_volatility,
        #         ) = vals
        #         last_price, bid, ask, change, change_percent, implied_volatility = map(
        #             lambda x: float(x.replace(",", "").replace("%", "")),
        #             [last_price, bid, ask, change, change_percent, implied_volatility],
        #         )
        #
        #         if (
        #             session.query(SPYFinanceOptions)
        #             .filter(SPYFinanceOptions.contract_name == contract_name)
        #             .count()
        #             != 0
        #         ):
        #             continue
        #
        #         dt = datetime.strptime(dt, "%m/%d/%Y %I:%M %p")
        #         results.append(
        #             SPYFinanceOptions(
        #                 contract_name=contract_name,
        #                 last_trade_date=dt,
        #                 strike=strike,
        #                 last_price=last_price,
        #                 bid=bid,
        #                 ask=ask,
        #                 change=change,
        #                 change_percent=change_percent,
        #                 volume=volume.replace(",", "") if volume != "-" else 0,
        #                 open_interest=open_interest.replace(",", ""),
        #                 implied_volatility=implied_volatility,
        #                 calls=calls,
        #                 in_the_money="inTheMoney" in row["class"],
        #             )
        #         )
        #     calls = not calls
        #
        # if results:
        #     session.bulk_save_objects(results)
        #     session.commit()
        #     logger.success("Done saving new records for Yahoo finance (SPY) Options")
        # else:
        #     logger.info(f"No records to be save - {raw_dt}")


def scrape_job(session):
    """
    Main job scraper function.

    :param session: sqlalchemy db session
    :return: None
    """
    logger.info("Scraping Yahoo finance (SPY) Options")
    # opt_toolbar = None
    # opts = []
    # retry = 0
    #
    # while not opt_toolbar and retry < 3:
    #     html_source = send_page_request()
    #     soup = BeautifulSoup(html_source, "html.parser")
    #     opt_toolbar = soup.find("div", {"data-testid": "options-toolbar"})
    #     logger.info("retrying...")
    #     retry += 1
    #     if retry == 3:
    #         return
    #     time.sleep(3)
    #
    # for opt in opt_toolbar.div.find("div", recursive=False):
    #     if opt := opt.text.strip(" "):
    #         opts.append(
    #             (
    #                 datetime.strptime(opt, "%b %d, %Y")
    #                 .replace(tzinfo=timezone.utc)
    #                 .timestamp(),
    #                 opt,
    #             )
    #         )

    scrape_live_data(session)


def job_wrapper(job: Callable, session: sqlalchemy.orm.session.sessionmaker):
    """
    Wraps job with dependencies needed to instantiate every call.

    :param job: job func
    :param session: DB session maker
    :return: None
    """
    with session() as db_session:
        job(db_session)


def main():
    """
    Main function that schedules the job every week days at 4:01 PM
    using New York time zone.
    :return: None
    """
    db_engine = init_db()
    Session = sessionmaker(bind=db_engine)
    schedule.every(30).seconds.do(job_wrapper, scrape_job, Session)
    # job_wrapper(scrape_job, Session)

    while True:
        next_run = schedule.idle_seconds()
        logger.info(
            f"Time till next run {time.strftime('%H:%M:%S', time.gmtime(next_run))}."
        )

        if next_run > 0:
            time.sleep(next_run)

        schedule.run_pending()


if __name__ == "__main__":
    main()
