import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def scrape_data(self):
        try:
            response = self.session.get(self.url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            data_div = soup.find('div', class_='data-class')

            if data_div:
                transformed_data = data_div.get_text(strip=True)
                return transformed_data
            else:
                raise Exception('Failed to retrieve data. Please check the HTML structure.')

        except requests.exceptions.HTTPError as e:
            raise Exception(f'HTTP Error occurred while sending the request: {str(e)}')

        except requests.exceptions.RequestException as e:
            raise Exception(f'An error occurred while sending the request: {str(e)}')


def main():
    url = 'https://www.example.com'
    scraper = WebScraper(url)

    try:
        transformed_data = scraper.scrape_data()
        print(transformed_data)

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()