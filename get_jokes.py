import requests

class Test_joke():
    '''Создание новой шутки'''

    def __init__(self):
        pass

    base_url = 'https://api.chucknorris.io/jokes'
    url_joke_random = 'https://api.chucknorris.io/jokes/random'

    def get_categories_list(self):
        '''Метод получения списка категорий шуток'''

        path_categories_list = '/categories'
        url_categories_list = self.base_url + path_categories_list
        print(f'URL для получения списка категорий шуток - {url_categories_list}')
        return requests.get(url_categories_list).json()

    def get_all_jokes_for_all_categories(self):
        '''Метод получения всех шуток для каждой категории шутки из списка'''

        categories_list = self.get_categories_list()
        print(f'Список шуток {categories_list}')

        for category in categories_list:
            self.get_joke_random_for_category(category)
            print('_' * 100)
        print('Тест успешно пройден!')

    def get_joke_random_for_category(self, category):
        '''Метод получения одной случайно шутки по конкретной категории'''

        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url_joke_random + path_random_joke_category
        print(f'URL- {url_random_joke_category} для получения случайной шутки из категории - {category} ')
        # Получаем ответ на запрос. Сравниваем статус код с ожидаемым статус кодом
        responce = requests.get(url_random_joke_category)
        print(f'Статус-код: {responce.status_code}')
        assert responce.status_code == 200, f'ОШИБКА, {responce.status_code} не равно 200'
        print('Статус-код корректен')
        # Получаем шутки из ответа
        check_joke = responce.json()
        joke_value = check_joke.get("value")
        print(joke_value)
        # Получаем категорию шутки. Сравниваем категорию шутки из ответа с запрошенной категорией шутки
        check_category = responce.json()
        category_value = check_category.get('categories')
        assert category_value[0] == category, f"Ошибка, {category_value[0]} не равно {category} "
        print("Категории равны")

start_test = Test_joke()
start_test.get_all_jokes_for_all_categories()