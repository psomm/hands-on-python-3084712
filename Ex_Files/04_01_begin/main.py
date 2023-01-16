import requests

r = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
    timeout=3)

last_twenty_years = r.json()[1][:20]

for year in last_twenty_years:
    display_width = year["value"] // 5_000_000
    print(f"{year['date']} {year['value']:,} Einwohner {'=' * display_width}")
