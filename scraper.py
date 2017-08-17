import html.parser
import re
import urllib.request
import threading
import sys

"A simple web scraper"
class Scraper:
    def run(self, site):
        print("Running")
        self.links = set()
        sites = self.scrape(site)
        return self.links
    def scrape(self, data):
        try:
            with urllib.request.urlopen(data) as response:
                data = str(response.read())
            link_re = re.compile("[A-Za-z]+://[A-Za-z0-9-_]+.[A-Za-z0-9-_:%&;\?#/.=]+")
            links = link_re.findall(data)
            for link in links:
                sys.stdout.write(link)
                x = threading.Thread(target=self.scrape, args=(link,))
                x.start()
                print(link)
        except:
            pass
if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.run(input())