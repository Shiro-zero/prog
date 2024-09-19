import requests
from bs4 import BeautifulSoup
from transformers import pipeline

url = 'http://example.com'
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    # Extract text from the webpage
    text = soup.get_text()

    # Create a summarization pipeline
    summarizer = pipeline('summarization')

    # Generate a summary
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

    print(summary[0]['summary_text'])
else:
    print(f'Failed to retrieve page. Status code: {response.status_code}')