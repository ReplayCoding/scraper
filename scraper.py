import html.parser
import re
import urllib.request
import threading
import sys
import csv
"A simple web scraper"
file = open("scrape.csv", "a")
writer = csv.writer(file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
class Scraper:
    def run(self, site):
        print("Running")
        self.links = set()
        sites = self.scrape(site)
        return self.links
    def scrape(self, data):
        orig_link = data
        try:
            with urllib.request.urlopen(data) as response:
                data = str(response.read())
            link_re = re.compile("[A-Za-z]+://[A-Za-z0-9-_]+.[A-Za-z0-9-_:%&;\?#/.=]+")
            links = link_re.findall(data)
            for i, link in enumerate(links):
                sys.stdout.write(link + "\n")
                writer.writerow([link, orig_link, i])
                x = threading.Thread(target=self.scrape, args=(link,))
                x.start()
        except:
            pass
if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.run(input(">> "))