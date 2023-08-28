import json
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, source = None):
        self.source = source
        self.data = []
        return

    def parse(self, html_content = None):
        if html_content is None:
            with open(self.source) as f:
                html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find_all("table")[0]
        table_rows = table.find_all("tr")
        table_headers = [header.get_text() for header in table_rows[0].find_all("th")]
        if table_headers[0] == 'No':
            table_headers[0] = ''
        for row in table_rows[1:]:
            data = dict()
            columns = [column.get_text().strip() for column in row.find_all("td")]
            for i, header in enumerate(table_headers):
                data[header] = columns[i]
            self.data.append(data)
        return

    def save(self, dest):
        with open(dest, 'wt') as f:
            f.write(json.dumps(self.data))
        return
