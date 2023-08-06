#!/usr/bin/python3

# Copyright 2018-2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

from datetime import datetime, date
import json
from random import randint

import pandas as pd
import pkg_resources
import requests
import unidecode
from lxml.html import fromstring

from investpy.utils.user_agent import get_random
from investpy.utils.data import Data

from investpy.data.crypto_data import cryptos_as_df, cryptos_as_list, cryptos_as_dict


def get_cryptos():
    """
    This function retrieves all the crypto data stored in `cryptos.csv` file, which previously was
    retrieved from Investing.com. Since the resulting object is a matrix of data, the crypto data is properly
    structured in rows and columns, where columns are the crypto data attribute names.

    Note that just some cryptos are available for retrieval, since Investing.com does not provide information
    from all the available ones, just the main ones.

    Returns:
        :obj:`pandas.DataFrame` - cryptos_df:
            The resulting :obj:`pandas.DataFrame` contains all the crypto data from every available crypto coin as 
            indexed in Investing.com from the information previously retrieved by investpy and stored on a csv file.

            So on, the resulting :obj:`pandas.DataFrame` will look like::

                name | symbol | currency
                -----|--------|----------
                xxxx | xxxxxx | xxxxxxxx 

    Raises:
        FileNotFoundError: raised if cryptos file was not found.
        IOError: raised when cryptos file is missing or empty.

    """

    return cryptos_as_df()


def get_cryptos_list():
    """
    This function retrieves all the crypto coin names stored in `cryptos.csv` file, which contains all the
    data from the crypto coins as previously retrieved from Investing.com. So on, this function will just return
    the crypto coin names which will be the main input parameters when it comes to crypto data retrieval functions
    from investpy.

    Note that just some cryptos are available for retrieval, since Investing.com does not provide information
    from all the available ones, just the main ones.

    Returns:
        :obj:`list` - cryptos_list:
            The resulting :obj:`list` contains the all the available crypto coin names as indexed in Investing.com 
            from the information previously retrieved by investpy and stored on a csv file.

            In case the information was successfully retrieved, the :obj:`list` of crypto coin names will look like::

                cryptos_list = ['Bitcoin', 'Ethereum', 'XRP', 'Bitcoin Cash', 'Tether', 'Litecoin', ...]

    Raises:
        FileNotFoundError: raised if cryptos file was not found.
        IOError: raised when cryptos file is missing or empty.
    
    """

    return cryptos_as_list()


def get_cryptos_dict(columns=None, as_json=False):
    """
    This function retrieves all the crypto information stored in the `cryptos.csv` file and formats it as a
    Python dictionary which contains the same information as the file, but every row is a :obj:`dict` and
    all of them are contained in a :obj:`list`. Note that the dictionary structure is the same one as the
    JSON structure. Some optional paramaters can be specified such as the columns or as_json, which are the 
    column names that want to be retrieved in case of needing just some columns to avoid unnecessary information
    load, and whether the information wants to be returned as a JSON object or as a dictionary; respectively.

    Note that just some cryptos are available for retrieval, since Investing.com does not provide information
    from all the available ones, just the main ones.

    Args:
        columns (:obj:`list`, optional):column names of the crypto data to retrieve, can be: <name, currency, symbol>
        as_json (:obj:`bool`, optional): if True the returned data will be a :obj:`json` object, if False, a :obj:`list` of :obj:`dict`.

    Returns:
        :obj:`list` of :obj:`dict` OR :obj:`json` - cryptos_dict:
            The resulting :obj:`list` of :obj:`dict` contains the retrieved data from every crypto coin as indexed in Investing.com from
            the information previously retrieved by investpy and stored on a csv file.

            In case the information was successfully retrieved, the :obj:`list` of :obj:`dict` will look like::

                cryptos_dict = {
                    'name': name,
                    'currency': currency,
                    'symbol': symbol,
                }

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid.
        FileNotFoundError: raised if cryptos file was not found.
        IOError: raised when cryptos file is missing or empty.

    """

    return cryptos_as_dict(columns=columns, as_json=as_json)


def get_crypto_recent_data(crypto, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves recent historical data from the introduced crypto from Investing.com. So on, the recent data
    of the introduced crypto will be retrieved and returned as a :obj:`pandas.DataFrame` if the parameters are valid 
    and the request to Investing.com succeeds. Note that additionally some optional parameters can be specified: as_json 
    and order, which let the user decide if the data is going to be returned as a :obj:`json` or not, and if the historical 
    data is going to be ordered ascending or descending (where the index is the date), respectively.

    Args:
        crypto (:obj:`str`): name of the crypto currency to retrieve data from.
        as_json (:obj:`bool`, optional):
            to determine the format of the output data, either a :obj:`pandas.DataFrame` if False and a :obj:`json` if True.
        order (:obj:`str`, optional): to define the order of the retrieved data which can either be ascending or descending.
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function can return either a :obj:`pandas.DataFrame` or a :obj:`json` object, containing the retrieved
            recent data of the specified crypto currency. So on, the resulting dataframe contains the open, high, low, 
            close and volume values for the selected crypto on market days and the currency in which those values are presented.

            The resulting recent data, in case that the default parameters were applied, will look like::

                Date || Open | High | Low | Close | Volume | Currency 
                -----||------|------|-----|-------|--------|----------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx 

            but in case that as_json parameter was defined as True, then the output will be::

                {
                    name: name,
                    recent: [
                        {
                            date: 'dd/mm/yyyy',
                            open: x,
                            high: x,
                            low: x,
                            close: x,
                            volume: x,
                            currency: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid or errored.
        IOError: raised if cryptos object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced crypto name was not found or did not match any of the existing ones.
        ConnectionError: raised if connection to Investing.com could not be established.
        IndexError: raised if crypto recent data was unavailable or not found in Investing.com.

    Examples:
        >>> investpy.get_crypto_recent_data(crypto='bitcoin')
                          Open     High     Low   Close   Volume Currency
            Date                                                         
            2019-10-25  7422.8   8697.7  7404.9  8658.3  1177632      USD
            2019-10-26  8658.4  10540.0  8061.8  9230.6  1784005      USD
            2019-10-27  9230.6   9773.2  9081.0  9529.6  1155038      USD
            2019-10-28  9530.1   9866.9  9202.5  9207.2  1039295      USD
            2019-10-29  9206.5   9531.3  9125.3  9411.3   918477      USD

    """

    if not crypto:
        raise ValueError("ERR#0083: crypto parameter is mandatory and must be a valid crypto name.")

    if not isinstance(crypto, str):
        raise ValueError("ERR#0084: crypto argument needs to be a str.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if order not in ['ascending', 'asc', 'descending', 'desc']:
        raise ValueError("ERR#0003: order argument can just be ascending (asc) or descending (desc), str type.")

    if not interval:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if not isinstance(interval, str):
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if interval not in ['Daily', 'Weekly', 'Monthly']:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'crypto', 'cryptos.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        cryptos = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0081: cryptos file not found or errored.")

    if cryptos is None:
        raise IOError("ERR#0082: cryptos not found or unable to retrieve.")

    crypto = crypto.strip()
    crypto = crypto.lower()

    if unidecode.unidecode(crypto) not in [unidecode.unidecode(value.lower()) for value in cryptos['name'].tolist()]:
        raise RuntimeError("ERR#0085: crypto currency: " + crypto + ", not found, check if it is correct.")

    status = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'status']
    if status == 'unavailable':
        raise ValueError("ERR#0086: the selected crypto currency is not available for retrieval in Investing.com.")

    crypto_name = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'name']
    crypto_id = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'id']
    crypto_currency = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'currency']

    header = crypto_name + ' Historical Data'

    params = {
        "curr_id": crypto_id,
        "smlID": str(randint(1000000, 99999999)),
        "header": header,
        "interval_sec": interval,
        "sort_col": "date",
        "sort_ord": "DESC",
        "action": "historical_data"
    }

    head = {
        "User-Agent": get_random(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    url = "https://www.investing.com/instruments/HistoricalDataAjax"

    req = requests.post(url, headers=head, data=params)

    if req.status_code != 200:
        raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

    root_ = fromstring(req.text)
    path_ = root_.xpath(".//table[@id='curr_table']/tbody/tr")
    result = list()

    if path_:
        for elements_ in path_:
            if elements_.xpath(".//td")[0].text_content() == 'No results found':
                raise IndexError("ERR#0087: crypto information unavailable or not found.")

            info = []

            for nested_ in elements_.xpath(".//td"):
                info.append(nested_.get('data-real-value'))

            crypto_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0])).date()), '%Y-%m-%d')
            
            crypto_close = float(info[1].replace(',', ''))
            crypto_open = float(info[2].replace(',', ''))
            crypto_high = float(info[3].replace(',', ''))
            crypto_low = float(info[4].replace(',', ''))

            crypto_volume = int(info[5])

            result.insert(len(result),
                          Data(crypto_date, crypto_open, crypto_high, crypto_low,
                               crypto_close, crypto_volume, crypto_currency))

        if order in ['ascending', 'asc']:
            result = result[::-1]
        elif order in ['descending', 'desc']:
            result = result

        if as_json is True:
            json_ = {
                'name': crypto_name,
                'recent':
                    [value.crypto_as_json() for value in result]
            }

            return json.dumps(json_, sort_keys=False)
        elif as_json is False:
            df = pd.DataFrame.from_records([value.crypto_to_dict() for value in result])
            df.set_index('Date', inplace=True)

            return df
    else:
        raise RuntimeError("ERR#0004: data retrieval error while scraping.")


def get_crypto_historical_data(crypto, from_date, to_date, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves historical data from the introduced crypto from Investing.com. So on, the historical data
    of the introduced crypto will be retrieved and returned as a :obj:`pandas.DataFrame` if the parameters are valid 
    and the request to Investing.com succeeds. Note that additionally some optional parameters can be specified: as_json 
    and order, which let the user decide if the data is going to be returned as a :obj:`json` or not, and if the historical 
    data is going to be ordered ascending or descending (where the index is the date), respectively.

    Args:
        crypto (:obj:`str`): name of the crypto currency to retrieve data from.
        from_date (:obj:`str`): date formatted as `dd/mm/yyyy`, since when data is going to be retrieved.
        to_date (:obj:`str`): date formatted as `dd/mm/yyyy`, until when data is going to be retrieved.
        as_json (:obj:`bool`, optional):
            to determine the format of the output data, either a :obj:`pandas.DataFrame` if False and a :obj:`json` if True.
        order (:obj:`str`, optional): to define the order of the retrieved data which can either be ascending or descending.
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function can return either a :obj:`pandas.DataFrame` or a :obj:`json` object, containing the retrieved
            historical data of the specified crypto currency. So on, the resulting dataframe contains the open, high, 
            low, close and volume values for the selected crypto on market days and the currency in which those values are presented.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency 
                -----||------|------|-----|-------|--------|----------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx 

            but if we define `as_json=True`, then the output will be::

                {
                    name: name,
                    historical: [
                        {
                            date: 'dd/mm/yyyy',
                            open: x,
                            high: x,
                            low: x,
                            close: x,
                            volume: x,
                            currency: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid or errored.
        IOError: raised if cryptos object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced crypto currency name was not found or did not match any of the existing ones.
        ConnectionError: raised if connection to Investing.com could not be established.
        IndexError: raised if crypto historical data was unavailable or not found in Investing.com.

    Examples:
        >>> investpy.get_crypto_historical_data(crypto='bitcoin', from_date='01/01/2018', to_date='01/01/2019')
                           Open     High      Low    Close  Volume Currency
            Date                                                           
            2018-01-01  13850.5  13921.5  12877.7  13444.9   78425      USD
            2018-01-02  13444.9  15306.1  12934.2  14754.1  137732      USD
            2018-01-03  14754.1  15435.0  14579.7  15156.6  106543      USD
            2018-01-04  15156.5  15408.7  14244.7  15180.1  110969      USD
            2018-01-05  15180.1  17126.9  14832.4  16954.8  141960      USD

    """

    if not crypto:
        raise ValueError("ERR#0083: crypto parameter is mandatory and must be a valid crypto name.")

    if not isinstance(crypto, str):
        raise ValueError("ERR#0084: crypto argument needs to be a str.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if order not in ['ascending', 'asc', 'descending', 'desc']:
        raise ValueError("ERR#0003: order argument can just be ascending (asc) or descending (desc), str type.")

    if not interval:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if not isinstance(interval, str):
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if interval not in ['Daily', 'Weekly', 'Monthly']:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    try:
        datetime.strptime(from_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("ERR#0011: incorrect from_date date format, it should be 'dd/mm/yyyy'.")

    try:
        datetime.strptime(to_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("ERR#0012: incorrect to_date format, it should be 'dd/mm/yyyy'.")

    start_date = datetime.strptime(from_date, '%d/%m/%Y')
    end_date = datetime.strptime(to_date, '%d/%m/%Y')

    if start_date >= end_date:
        raise ValueError("ERR#0032: to_date should be greater than from_date, both formatted as 'dd/mm/yyyy'.")

    date_interval = {
        'intervals': [],
    }

    flag = True

    while flag is True:
        diff = end_date.year - start_date.year

        if diff > 20:
            obj = {
                'start': start_date.strftime('%m/%d/%Y'),
                'end': start_date.replace(year=start_date.year + 20).strftime('%m/%d/%Y'),
            }

            date_interval['intervals'].append(obj)

            start_date = start_date.replace(year=start_date.year + 20)
        else:
            obj = {
                'start': start_date.strftime('%m/%d/%Y'),
                'end': end_date.strftime('%m/%d/%Y'),
            }

            date_interval['intervals'].append(obj)

            flag = False

    interval_limit = len(date_interval['intervals'])
    interval_counter = 0

    data_flag = False

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'crypto', 'cryptos.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        cryptos = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0081: cryptos file not found or errored.")

    if cryptos is None:
        raise IOError("ERR#0082: cryptos not found or unable to retrieve.")

    crypto = crypto.strip()
    crypto = crypto.lower()

    if unidecode.unidecode(crypto) not in [unidecode.unidecode(value.lower()) for value in cryptos['name'].tolist()]:
        raise RuntimeError("ERR#0085: crypto currency: " + crypto + ", not found, check if it is correct.")

    status = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'status']
    if status == 'unavailable':
        raise ValueError("ERR#0086: the selected crypto currency is not available for retrieval in Investing.com.")

    crypto_name = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'name']
    crypto_id = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'id']
    crypto_currency = cryptos.loc[(cryptos['name'].str.lower() == crypto).idxmax(), 'currency']

    header = crypto_name + ' Historical Data'

    final = list()

    for index in range(len(date_interval['intervals'])):
        interval_counter += 1

        params = {
            "curr_id": crypto_id,
            "smlID": str(randint(1000000, 99999999)),
            "header": header,
            "st_date": date_interval['intervals'][index]['start'],
            "end_date": date_interval['intervals'][index]['end'],
            "interval_sec": interval,
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }

        head = {
            "User-Agent": get_random(),
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "text/html",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        url = "https://www.investing.com/instruments/HistoricalDataAjax"

        req = requests.post(url, headers=head, data=params)

        if req.status_code != 200:
            raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

        if not req.text:
            continue

        root_ = fromstring(req.text)
        path_ = root_.xpath(".//table[@id='curr_table']/tbody/tr")

        result = list()

        if path_:
            for elements_ in path_:
                if elements_.xpath(".//td")[0].text_content() == 'No results found':
                    if interval_counter < interval_limit:
                        data_flag = False
                    else:
                        raise IndexError("ERR#0087: crypto information unavailable or not found.")
                else:
                    data_flag = True
                
                info = []
            
                for nested_ in elements_.xpath(".//td"):
                    info.append(nested_.get('data-real-value'))

                if data_flag is True:
                    crypto_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0])).date()), '%Y-%m-%d')
            
                    crypto_close = float(info[1].replace(',', ''))
                    crypto_open = float(info[2].replace(',', ''))
                    crypto_high = float(info[3].replace(',', ''))
                    crypto_low = float(info[4].replace(',', ''))

                    crypto_volume = int(info[5])

                    result.insert(len(result),
                                  Data(crypto_date, crypto_open, crypto_high, crypto_low,
                                       crypto_close, crypto_volume, crypto_currency))

            if data_flag is True:
                if order in ['ascending', 'asc']:
                    result = result[::-1]
                elif order in ['descending', 'desc']:
                    result = result

                if as_json is True:
                    json_ = {
                        'name': crypto_name,
                        'historical':
                            [value.crypto_as_json() for value in result]
                    }
                    
                    final.append(json_)
                elif as_json is False:
                    df = pd.DataFrame.from_records([value.crypto_to_dict() for value in result])
                    df.set_index('Date', inplace=True)

                    final.append(df)
        else:
            raise RuntimeError("ERR#0004: data retrieval error while scraping.")

    if as_json is True:
        return json.dumps(final[0], sort_keys=False)
    elif as_json is False:
        return pd.concat(final)


def search_cryptos(by, value):
    """
    This function searches cryptos by the introduced value for the specified field. This means that this function
    is going to search if there is a value that matches the introduced one for the specified field which is the
    `cryptos.csv` column name to search in. Available fields to search cryptos are 'name' and 'symbol'.

    Args:
        by (:obj:`str`): name of the field to search for, which is the column name which can be: 'name' or 'symbol'.
        value (:obj:`str`): value of the field to search for, which is the value that is going to be searched.

    Returns:
        :obj:`pandas.DataFrame` - search_result:
            The resulting :obj:`pandas.DataFrame` contains the search results from the given query, which is
            any match of the specified value in the specified field. If there are no results for the given query,
            an error will be raised, but otherwise the resulting :obj:`pandas.DataFrame` will contain all the
            available cryptos that match the introduced query.

    Raises:
        ValueError: raised if any of the introduced parameters is not valid or errored.
        IOError: raised if data could not be retrieved due to file error.
        RuntimeError: raised if no results were found for the introduced value in the introduced field.

    """

    available_search_fields = ['name', 'symbol']

    if not by:
        raise ValueError('ERR#0006: the introduced field to search is mandatory and should be a str.')

    if not isinstance(by, str):
        raise ValueError('ERR#0006: the introduced field to search is mandatory and should be a str.')

    if isinstance(by, str) and by not in available_search_fields:
        raise ValueError('ERR#0026: the introduced field to search can either just be '
                         + ' or '.join(available_search_fields))

    if not value:
        raise ValueError('ERR#0017: the introduced value to search is mandatory and should be a str.')

    if not isinstance(value, str):
        raise ValueError('ERR#0017: the introduced value to search is mandatory and should be a str.')

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'crypto', 'cryptos.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        cryptos = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0081: cryptos file not found or errored.")

    if cryptos is None:
        raise IOError("ERR#0082: cryptos not found or unable to retrieve.")

    cryptos['matches'] = cryptos[by].str.contains(value, case=False)

    search_result = cryptos.loc[cryptos['matches'] == True].copy()

    if len(search_result) == 0:
        raise RuntimeError('ERR#0043: no results were found for the introduced ' + str(by) + '.')

    search_result.drop(columns=['tag', 'id', 'matches'], inplace=True)
    search_result.reset_index(drop=True, inplace=True)

    return search_result
