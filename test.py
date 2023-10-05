import requests
import csv
import xml.etree.ElementTree as ET
import pandas as pd

xml_data = '''
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom" xml:base="https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml">
<title type="text">DailyTreasuryYieldCurveRateData</title>
<id>https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml-item?data=daily_treasury_yield_curve</id>
<updated>2023-10-03T15:51:03Z</updated>
<link rel="self" title="DailyTreasuryYieldCurveRateData" href="DailyTreasuryYieldCurveRateData"/>
<entry>
<title type="text"/>
<updated>2023-10-03T15:51:03Z</updated>
<author>
<name/>
</author>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties>
<d:NEW_DATE m:type="Edm.DateTime">2023-10-02T00:00:00</d:NEW_DATE>
<d:BC_1MONTH m:type="Edm.Double">5.56</d:BC_1MONTH>
<d:BC_2MONTH m:type="Edm.Double">5.60</d:BC_2MONTH>
<d:BC_3MONTH m:type="Edm.Double">5.62</d:BC_3MONTH>
<d:BC_4MONTH m:type="Edm.Double">5.62</d:BC_4MONTH>
<d:BC_6MONTH m:type="Edm.Double">5.58</d:BC_6MONTH>
<d:BC_1YEAR m:type="Edm.Double">5.49</d:BC_1YEAR>
<d:BC_2YEAR m:type="Edm.Double">5.12</d:BC_2YEAR>
<d:BC_3YEAR m:type="Edm.Double">4.88</d:BC_3YEAR>
<d:BC_5YEAR m:type="Edm.Double">4.72</d:BC_5YEAR>
<d:BC_7YEAR m:type="Edm.Double">4.73</d:BC_7YEAR>
<d:BC_10YEAR m:type="Edm.Double">4.69</d:BC_10YEAR>
<d:BC_20YEAR m:type="Edm.Double">5.00</d:BC_20YEAR>
<d:BC_30YEAR m:type="Edm.Double">4.81</d:BC_30YEAR>
<d:BC_30YEARDISPLAY m:type="Edm.Double">4.81</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry>
<title type="text"/>
<updated>2023-10-03T15:51:03Z</updated>
<author>
<name/>
</author>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties>
<d:NEW_DATE m:type="Edm.DateTime">2023-10-03T00:00:00</d:NEW_DATE>
<d:BC_1MONTH m:type="Edm.Double">5.55</d:BC_1MONTH>
<d:BC_2MONTH m:type="Edm.Double">5.60</d:BC_2MONTH>
<d:BC_3MONTH m:type="Edm.Double">5.62</d:BC_3MONTH>
<d:BC_4MONTH m:type="Edm.Double">5.62</d:BC_4MONTH>
<d:BC_6MONTH m:type="Edm.Double">5.58</d:BC_6MONTH>
<d:BC_1YEAR m:type="Edm.Double">5.49</d:BC_1YEAR>
<d:BC_2YEAR m:type="Edm.Double">5.15</d:BC_2YEAR>
<d:BC_3YEAR m:type="Edm.Double">4.95</d:BC_3YEAR>
<d:BC_5YEAR m:type="Edm.Double">4.80</d:BC_5YEAR>
<d:BC_7YEAR m:type="Edm.Double">4.84</d:BC_7YEAR>
<d:BC_10YEAR m:type="Edm.Double">4.81</d:BC_10YEAR>
<d:BC_20YEAR m:type="Edm.Double">5.13</d:BC_20YEAR>
<d:BC_30YEAR m:type="Edm.Double">4.95</d:BC_30YEAR>
<d:BC_30YEARDISPLAY m:type="Edm.Double">4.95</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
</feed>
'''

root = ET.fromstring(xml_data)
properties = root.findall('.//{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties')


def remove_namespace(tag):
    return tag.split('}')[1] if '}' in tag else tag

yc_data = []

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

df = pd.DataFrame(yc_data)
df.to_csv("treasury_yield_curve.csv")