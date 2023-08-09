import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time

# указатель позиции чтения цитаты: номер страницы и номер цитаты на странице
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
        """
        Получить html - страницу с номером page
        :param page: номер страницы
        :return: страницу как текст
        """
        nonlocal url
        header = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
            'Accept':
                'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8'
        }
        full_url = url + f'page/{page}/'  # получить полный url: базовый + номер страницы
        response = requests.get(full_url, headers=header)  # загрузить страницу
        if response.status_code == 200:  # если успешно
            return response.text  # получить страницу как текст
        else:
            return None

    def get_one_quote(html, quote_number) -> tuple | None:
        """
        Получить цитату с конкретным номером
        :param html: страница как текст
        :param quote_number: номер цитаты
        :return: кортеж (цитата, автор)
        """
        soup = BeautifulSoup(html, 'html.parser')  # загрузить страницу в парсер
        quote_list = soup.find_all(name='div', attrs={'class': 'quote'})  # найти все цитаты
        if quote_number in range(1, len(quote_list) + 1):
            # выделить из цитаты с нужным номером текст и автора
            text = quote_list[quote_number - 1].find(name='span', attrs={'itemprop': 'text'}).text
            author = quote_list[quote_number - 1].find(name='small', attrs={'itemprop': 'author'}).text
            return text, author
        else:
            return None

    def get_all_quotes_on_page(html) -> list[tuple]:
        """
        Получить все цитаты на странице
        :param html: страница как текст
        :return: список кортежей (цитата, автор)
        """
        result = []
        soup = BeautifulSoup(html, 'html.parser')  # загрузить страницу в парсер
        quote_list = soup.find_all(name='div', attrs={'class': 'quote'})  # найти все цитаты
        for quote in quote_list:
            # сформировать список кортежей (цитата, автор)
            result.append(
                (quote.find(name='span', attrs={'itemprop': 'text'}).text,
                 quote.find(name='small', attrs={'itemprop': 'author'}).text,)
            )
        return result

    global pointer  # позицию чтения цитаты храним во внешней переменной, можно также в базе данных

    result = []
    quotes_need_read_on_page = quote_qty  # установить кол-во цитат, которые нужно считать на текущей странице
    success = False  # сбросить флаг успешного окончания процесса

    while not success:
        html = get_page(page=pointer['page'])  # прочитать страницу
        quotes = get_all_quotes_on_page(html)  # прочитать все цитаты со страницы
        if not quotes:  # если более нет цитат
            print('The END achieved!')
            return result

        start = pointer['quote_num'] - 1  # установить номер первой цитаты, которую нужно прочесть
        finish = start + quotes_need_read_on_page  # установить номер последней цитаты, которую нужно прочесть
        quotes_for_add = quotes[start:finish]  # выделить из списка всех цитат на странице только те, что нужны
        result.extend(quotes_for_add)  # добавить к результату
        quotes_been_read = len(quotes_for_add)  # сколько было прочитано цитат с текущей страницы?
        pointer['quote_num'] += quotes_been_read  # сдвинуть позицию чтения на количество прочитанных цитат

        if quotes_been_read < quotes_need_read_on_page:  # если с текущей страницы было прочитано меньше цитат, чем требовалось
            pointer['page'] += 1  # установить позицию чтения на начало следующей страницы
            pointer['quote_num'] = 1
            quotes_need_read_on_page -= quotes_been_read  # Установить количество цитат,
                                                          # которые осталось прочесть в текущем цикле чтения.
                                                          # Вернуться в начало цикла чтения
        else:  # если прочитали сколько требовалось
            success = True  # установить флаг успешного окончания процесса
            if pointer['quote_num'] > len(quotes):  # если на текущей странице не осталось непрочитанных цитат,
                pointer['page'] += 1  # установить позицию чтения на начало следующей страницы
                pointer['quote_num'] = 1

    return result



def main():
    url = r'https://quotes.toscrape.com/'  # адрес, откуда читаем цитаты
    for _ in range(13):  # читаем 13 раз по 9 цитат за 1 раз и выводим на печать
        print(*get_data(url=url, quote_qty=9), sep='\n', end='\n' * 2)


if __name__ == '__main__':
    main()
