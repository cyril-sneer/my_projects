import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time

pointer = {'page': 1,
           'quote_num': 1}

def test_eight_components():
    # service = ChromeService(executable_path='c:\\Downloads\\chrome-win64\\chrome.exe')
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()

def get_data_by_selenium():
    # service = ChromeService(executable_path=r'c:\Downloads\chrome-win64\chrome.exe')
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    url = 'https://www.auchan.fr/recherche?text=ARBRE+A+CHAT'
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    with open('draft.html', 'w') as file:
        file.write(html)
    driver.close()

def get_data(url, quote_qty=5):

    def get_page(page):
        nonlocal url
        header = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept':
                'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8'
        }
        full_url = url + f'page/{page}/'
        response = requests.get(full_url, headers=header)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_one_quote(html, quote_number) -> tuple | None:
        soup = BeautifulSoup(html, 'html.parser')
        quote_list = soup.find_all(name='div', attrs={'class': 'quote'})
        if quote_number in range(1, len(quote_list) + 1):
            text = quote_list[quote_number - 1].find(name='span', attrs={'itemprop': 'text'}).text
            author = quote_list[quote_number - 1].find(name='small', attrs={'itemprop': 'author'}).text
            return text, author
        else:
            return None

    def get_all_quotes_on_page(html) -> list[tuple]:
        result = []
        soup = BeautifulSoup(html, 'html.parser')
        quote_list = soup.find_all(name='div', attrs={'class': 'quote'})
        for quote in quote_list:
            result.append(
                (quote.find(name='span', attrs={'itemprop': 'text'}).text,
                 quote.find(name='small', attrs={'itemprop': 'author'}).text,)
            )
        return result

    global pointer

    result = []
    quotes_need_read_on_page = quote_qty
    success = False

    while not success:
        html = get_page(page=pointer['page'])
        quotes = get_all_quotes_on_page(html)
        if not quotes:
            print('The END achieved!')
            return result

        start = pointer['quote_num'] - 1
        finish = start + quotes_need_read_on_page
        quotes_for_add = quotes[start:finish]
        result.extend(quotes_for_add)
        quotes_been_read = len(quotes_for_add)
        pointer['quote_num'] += quotes_been_read

        if quotes_been_read < quotes_need_read_on_page:
            pointer['page'] += 1
            pointer['quote_num'] = 1
            quotes_need_read_on_page -= quotes_been_read
        else:
            success = True
            if pointer['quote_num'] > len(quotes):
                pointer['page'] += 1
                pointer['quote_num'] = 1

    return result



def main():
    url = r'https://quotes.toscrape.com/'
    for _ in range(13):
        print(*get_data(url=url, quote_qty=9), sep='\n', end='\n' * 2)


if __name__ == '__main__':
    main()
