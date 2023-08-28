if __name__ == "__main__":
    from download import Downloader
    from parse import Parser
    from data import Provider
else:
    from .download import Downloader
    from .parse import Parser
    from .data import Provider

def process(url, web_page_path = None, data_path = None, key = None):
    downloader = Downloader(url)
    downloader.get_html()
    if web_page_path is not None:
        downloader.save(web_page_path)

    parser = Parser()
    parser.parse(downloader.html_content)
    if data_path is not None:
        parser.save(data_path)

    provider = Provider()
    provider.data = parser.data
    if key is not None:
        provider.sort(key)
    return provider.to_csv()
