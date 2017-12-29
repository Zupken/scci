import lxml.html
import requests
import scraper as sc


class Scraping:

    def __init__(self):
        self.default_url = 'http://scci.com.pk/member-detail.php?id='
        self.number = 1
        self.data = []
        self.url = lambda number: self.default_url+number

    def get_data(self):
        for number in range(1, 9700):
            self.current_info = []
            print(self.number)
            self.source = requests.get(self.url(str(self.number)))
            self.tree  = lxml.html.fromstring(self.source.content)
            self.etree = self.tree.xpath('//table//table//tr[position() < 12]')
            for index, element in enumerate(self.etree):
                self.current_info.append(sc.first_value(element.xpath('./td[2]//text()')))
            self.data.append(self.current_info)
            self.number += 1
        sc.Database(('Company', 'Member ID', 'Contact person', 'Designation', 'Product category', 'Address', 'Phone', 'Mobile', 'Fax', 'Email', 'Web')).push_data(self.data)


Scraping = Scraping()
Scraping.get_data()
