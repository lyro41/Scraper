import json

class Provider:
    def __init__(self):
        return

    def load(self, source):
        with open(source) as f:
            self.data = json.load(f)
        return

    def sort(self, key = lambda country: country[list(country)[0]]):
        self.data.sort(key = key)
        return

    def to_csv(self):
        headers = [key for key in self.data[0]]
        csv = ", ".join(headers) + '\n'
        for country in self.data:
            row = [country[key] for key in headers]
            csv += ", ".join(row) + '\n'
        return csv

