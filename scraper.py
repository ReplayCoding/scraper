import html.parser
import re
import urllib.request
import threading
import sys
import csv
import os

"A simple web scraper"
file = open("scrape.csv", "a")
writer = csv.writer(file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
class Scraper:
    def run(self, site):
        print("Running")
        self.count = 0
        sites = self.scrape(site)
        return sites
    def scrape(self, data):
        if self.count >= 1000:
            print("done")
            os._exit(0)
        orig_link = data
        try:
            with urllib.request.urlopen(data) as response:
                data = str(response.read())
            link_re = re.compile("[A-Za-z]+://[A-Za-z0-9-_]+.[A-Za-z0-9-_:%&;\?#/.=]+")
            links = link_re.findall(data)
            for i, link in enumerate(links):
                self.count += 1
                sys.stdout.write("{0}:{1}\n".format(str(self.count), link))
                writer.writerow([link, orig_link, i])
                x = threading.Thread(target=self.scrape, args=(link,))
                x.start()
        except:
            pass
            #raise
if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.run(("https://github.com"))