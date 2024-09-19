import requests
from bs4 import BeautifulSoup
import csv
from transformers import pipeline
import io

sauter le nav

def summarize(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=200, min_length=10, do_sample=False)[0]['summary_text']
    return summary


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
        length = round(len(body)/2)
        body_resume = summarize(body[:length])
        return {
            'url': url,
            'title': title,
            'body_resume': body_resume,
            'body': body
        }
    except Exception as e:
        print(f"Failed to scrape {url}: {str(e)}")
        return None


def write_results(filename, results):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'title', 'body_resume', 'body'])
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
