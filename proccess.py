import requests
import csv
import xml.etree.ElementTree as ET
import pandas as pd
from utils import remove_namespace
import requests
from datetime import date, timedelta

def update_yield_curve_data(year_list=[]):
    previous_day = date.today() - timedelta(days=2)
    previous_day_str = previous_day.strftime("%Y-%m-%d")

    download_path = './data/DFEDTARU.csv'
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFEDTARU&cosd={previous_day_str}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully as '{download_path}'")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

    download_path = './data/DFEDTARL.csv'
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFEDTARL&cosd={previous_day_str}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully as '{download_path}'")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

    yc_data = []
    base_url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value="
    for y in year_list:
        url = base_url + str(y)
        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            root = ET.fromstring(response.text)
            properties = root.findall('.//{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties')
            for p in properties:
                temp = dict()
                for child in p:
                    tag = remove_namespace(child.tag)
                    value = child.text
                    if tag == "NEW_DATE":
                        temp[tag] = pd.to_datetime(value)
                    else:
                        temp[tag] = float(value)
                yc_data.append(temp)
        else:
            print(f"request failed for year: {y}")
            return False

    if yc_data:
        df = pd.DataFrame(yc_data)
        df_sorted = df.sort_values(by='NEW_DATE', ascending=False)
        df_sorted.to_csv("./data/treasury_yield_curve.csv")
    else:
        return False
    return True

def bsm_option_price(S, K, sigma, T, r, option_type):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type")

    return option_price