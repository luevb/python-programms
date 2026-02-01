import requests
from urllib.parse import urljoin


def main():
    url = input('Ссылка: ')

    with open('checks.txt') as f:
        links = [line.strip() for line in f if line.strip()] #Удаляем пустые строки, пробелы и создаем список.

    if len(links) == 0:
        print('Нет ссылок для проверки')
        return

    for link in links:
        full_link = urljoin(url, link)
        response = requests.get(full_link) #Отправляем запрос
        if response.status_code != 404:
            print(f'{full_link} - найден')


if __name__ == "__main__":
    main()
