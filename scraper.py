from bs4 import BeautifulSoup
import requests

class Scraper:

    def find_jobs(self) -> dict:
        # HTTP Request
        result = requests.get(url='https://realpython.github.io/fake-jobs/', verify=False)

        # Web Scraper
        scraper = BeautifulSoup(result.content, 'html.parser')
        cards = scraper.find(id='ResultsContainer').find_all('div', class_='card-content')
        
        jobs = []
        index = 0
        # Create JSON objects
        for card in cards:
            item = {
                'title' : card.find('h2', class_='title is-5').text.strip(),
                'company': card.find('h3', class_='subtitle is-6 company').text.strip(),
                'location': card.find('p', class_='location').text.strip(),
                'date-posted': card.find('time').text.strip()
            }
            
            jobs.append(item)

        return jobs