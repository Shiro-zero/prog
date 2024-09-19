import requests
from bs4 import BeautifulSoup
import csv
import io


def read_links(filename):
    links = []
    with open(filename, 'r') as f:
        for link in f:
            links.append(link.strip())
    return links


def scrape_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        body = ' '.join([p.text for p in soup.body.find_all('p')])
        return {
            'url': url,
            'title': title,
            'body': body
        }
    except Exception as e:
        print(f"Failed to scrape {url}: {str(e)}")
        return None


def write_results(filename, results):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'title', 'body'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)


def main():
    link_file = 'links.txt'
    output_file = 'results.csv'

    links = read_links(link_file)
    results = [scrape_page(link) for link in links]

    write_results(output_file, results)


if __name__ == '__main__':
    main()
