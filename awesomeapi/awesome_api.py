import requests

from awesomeapi.exceptions import NotFoundError

AWESOME_API_URL_BASE = 'https://economia.awesomeapi.com.br'
AWESOME_API_JSON = 'json'
AWWSOME_API_XML = 'xml'


def get_ticker(ticker):
    """
    Get ticker information
    :param ticker: Ticker to get information
    :return: Ticker information
    """
    req = requests.get('{base}/{type}/{time}/{ticker}'.format(base=AWESOME_API_URL_BASE, type=AWESOME_API_JSON,
                                                              time='last', ticker=ticker))
    if req.status_code == 200:
        return req.json()
    else:
        raise NotFoundError('Ticker not found')


def get_history_ticker(ticker, qtd_days):
    """
    Get ticker history information
    :param ticker: Ticker to get information
    :param qtd_days: Quantity of days to get information
    :return: Ticker history information

    """
    req = requests.get('{base}/{type}/{time}/{ticker}/{days}'.format(base=AWESOME_API_URL_BASE, type=AWESOME_API_JSON,
                                                                     time='daily', ticker=ticker,
                                                                     days=str(qtd_days)))
    if req.status_code == 200:
        return req.json()
    else:
        raise NotFoundError('Ticker not found')


def get_all_tickers():
    """
    Get all tickers available
    :return: All tickers information

    """
    req = requests.get('{base}/{type}/available/uniq'.format(base=AWESOME_API_URL_BASE, type=AWESOME_API_JSON))
    if req.status_code == 200:
        return req.json()
    else:
        raise NotFoundError('Ticker not found')


def get_all_available_combinations():
    """
    Get all available combinations
    :return: All available combinations
    """
    req = requests.get('{base}/{type}/available'.format(base=AWESOME_API_URL_BASE, type=AWESOME_API_JSON))
    if req.status_code == 200:
        return req.json()
    else:
        raise NotFoundError('Ticker not found')
