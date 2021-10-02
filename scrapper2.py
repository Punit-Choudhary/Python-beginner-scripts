import requests
from bs4 import BeautifulSoup

def price():
    URL = 'https://finance.yahoo.com/quote/BTC-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAKag91Xt7nUXOyMx3LF2u6obPjWGNprSxdZxgB8EAOz76XNxSTEVyfIgzvYxqMhbL8YIxWACcoMkcPsnyFhvqp4OZSgDY8CqIiwKfw_kUZ-S095-kZvmncLFS56Rl3wsm3Ls8JtfVigvVWeU-7kU9KhDGsfZYMv_-p_z8OU0ttSD'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = []
    for element in soup.findAll(attrs="D(ib) Mend(20px)"):
        price = element.find('span')
        if price not in results:
            results.append(price.text)
            bitcoin = "Bitcoin Price: " + results[0]
            print(bitcoin)
price()