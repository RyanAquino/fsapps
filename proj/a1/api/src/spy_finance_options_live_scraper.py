import time
from datetime import datetime, timezone
from typing import Callable

import requests
import schedule
import sqlalchemy
from loguru import logger
from models import SPYFinanceOptions, init_db
from sqlalchemy.orm import sessionmaker


def send_api_request(ts: int = None):
    """
    Send API requests to yahoo finance v6 API.

    :param ts: timestamp
    :return:  response done or None
    """
    params = {"formatted": True, "straddle": False, "en": "US", "region": "US"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    }

    if ts:
        params["date"] = ts

    try:
        response = requests.get(
            "https://query1.finance.yahoo.com/v6/finance/options/%5ESPX",
            params=params,
            headers=headers,
        )
        response_data = response.json()
        return response_data.get("optionChain", {}).get("result")[0]
    except requests.exceptions.RequestException as e:
        logger.warning(f"Exception raised when sending HTTP requests: {str(e)}")
        return None


def scrape_live_data(session):
    """
    Scrape live data of yahoo finance (SPY) SPX options
    """
    logger.info("Scraping Yahoo finance (SPY) Options")
    response = send_api_request()

    if not response:
        return

    opts = response.get("expirationDates")

    for opt in opts:
        raw_dt = datetime.fromtimestamp(opt, timezone.utc).date()
        response = send_api_request(opt)

        if not response:
            continue

        idx_opt = response.get("options")[0]
        results = []

        for item in idx_opt.get("calls"):
            contract_name = item.get("contractSymbol")

            if (
                session.query(SPYFinanceOptions)
                .filter(SPYFinanceOptions.contract_name == contract_name)
                .count()
                != 0
            ):
                continue

            results.append(
                SPYFinanceOptions(
                    contract_name=contract_name,
                    last_trade_date=datetime.fromtimestamp(
                        item.get("lastTradeDate").get("raw"), timezone.utc
                    ),
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
            contract_name = item.get("contractSymbol")
            if (
                session.query(SPYFinanceOptions)
                .filter(SPYFinanceOptions.contract_name == contract_name)
                .count()
                != 0
            ):
                continue

            results.append(
                SPYFinanceOptions(
                    contract_name=contract_name,
                    last_trade_date=datetime.fromtimestamp(
                        item.get("lastTradeDate").get("raw"), timezone.utc
                    ),
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
    Main function
    """
    db_engine = init_db()
    Session = sessionmaker(bind=db_engine)
    schedule.every(30).seconds.do(job_wrapper, scrape_live_data, Session)

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
