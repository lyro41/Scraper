import requests

class Downloader:
     def __init__(self, url, params = {}, method = "GET"):
          self.url = url
          self.params = params
          self.method = method
          return

     def get_html(self):
          if self.method == "GET":
               self.html_content = requests.get(self.url, self.params).content
               return 
          raise ValueError('could not form get request with method not equal to "GET"')

     def save(self, path):
          with open(path, "wb") as f:
               f.write(self.html_content)
          return
