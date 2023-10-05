import requests
import csv
import xml.etree.ElementTree as ET
import pandas as pd
from utils import remove_namespace


def update_yield_curve_data(year_list=[]):
    # url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value_month=202310"
    yc_data = []
    print(year_list)
    base_url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value"
    for y in year_list:
        url = base_url + str(y)
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
        
    df = pd.DataFrame(yc_data)
    df.to_csv("./data/treasury_yield_curve.csv")
    return "complete"