import requests
from bs4 import BeautifulSoup
import csv

def get_animals_count():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letter_counts = {}

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        category_block = soup.find('div', class_='mw-category-columns')
        if not category_block:
            break
            
        groups = category_block.find_all('div', class_='mw-category-group')
        
        for group in groups:
            letter = group.find('h3').text.strip()
            if not letter.isalpha() or not letter.isupper():
                continue
                
            items = group.find_all('li')
            letter_counts[letter] = letter_counts.get(letter, 0) + len(items)
        
        next_page = soup.find('a', text='Следующая страница')
        if not next_page:
            break
            
        url = "https://ru.wikipedia.org" + next_page['href']
    
    return letter_counts

def save_to_csv(counts):
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])


if __name__ == "__main__":
    counts = get_animals_count()
    save_to_csv(counts)
