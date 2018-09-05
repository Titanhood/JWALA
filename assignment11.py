import requests
import json
a = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=435251")
b = json.loads(a.text)
print(a)
print(a.status_code)
print(a.content)
print(b["quoteText"]) 
