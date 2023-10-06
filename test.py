import requests
from datetime import date, timedelta

previous_day = date.today() - timedelta(days=1)
previous_day_str = previous_day.strftime("%Y-%m-%d")

# Customize the download path
download_path = f"custom_path/fred_data_{previous_day_str}.csv"  # Change 'custom_path' to your desired path

# Construct the URL with the previous day's date
url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFEDTARU&cosd={previous_day_str}"

response = requests.get(url)

if response.status_code == 200:
    with open(download_path, "wb") as file:
        file.write(response.content)
    print(f"File downloaded successfully as '{download_path}'")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
