import csv
# print to the console (pprint == pretty print objects)
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,\
    "for his services to Theoretical Physics, \
        and especially for his discovery of the law of the photoelectric effect",physics,1921'

# 'dict' similar to JSON for software apps
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r", encoding='utf8') as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Curie":
        pprint(laureate)
        break
