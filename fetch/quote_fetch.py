import requests
from bs4 import BeautifulSoup

base_link = "https://www.quoteambition.com/art-of-war-quotes/"

quotes_file = open("../data/all_quotes.txt", "w")

page = requests.get(base_link)
soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup.find_all('p')
for quote in quotes:
    if any(char.isdigit() for char in quote.text):
        quotes_file.write(".".join(quote.text.strip().split(".")[1:])[1:] + "|| - Sun Tzu, The Art of War" + "\n")

quotes_file.close()
