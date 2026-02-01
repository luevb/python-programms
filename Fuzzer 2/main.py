import requests
from urllib.parse import urljoin

# главная функция с основным кодом программы
def main():
    filters = input('Введите расширения файлов(через пробел и точкой вначале, например(.txt .php .yml)): ')
    url = input('Введите ссылку: ')
    filters = filters.split(' ')
    file_name = 'common-files.txt'

    # загружаем все ссылки из файла
    with open(file_name, 'rt') as f:
        extension = [line.strip() for line in f if line.strip()]

    # фильтруем расширения и записываем их в отдельный файл
    check_file = open('check.txt', 'w')
    for links in extension:
        for temp in filters:
            if temp in links:
                check_file.write(links + '\n')
    check_file.close()

    # загружаем все сортированные расширения из файла
    with open('check.txt', 'rt') as f:
        list_ext = [line.strip() for line in f if line.strip()]

    result_file = open('result.txt', 'w')

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    for link in list_ext:
        full_url = urljoin(url, link)
        response = requests.get(full_url, headers=headers)
        if response.status_code != 404:
            print(f'Найдено совпадение: {full_url} (статус {response.status_code})')
            result_file.write(full_url + '\n')


    result_file.close()
if __name__ == "__main__":
    main()