import threading
import requests


def scrape_website(url):
	response = requests.get(url)
	print(f"Scraped {url}: {len(response.text)} characters")

urls ["https://github.com","https://instagram.com"]
threads = []


for url in urls:
	t = threading.Thread(target=scrape_website, args=(url,))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print("All websites scraped")
