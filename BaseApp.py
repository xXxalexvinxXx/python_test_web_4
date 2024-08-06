import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Чтение конфигурации из файла testdata.yaml
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata["address"]

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def get_element_property(self, locator, prop):
        element = self.find_element(locator)
        return element.value_of_css_property(prop)

    def go_to_site(self):
        return self.driver.get(self.base_url)


class BaseAPI:
    def __init__(self):
        self.base_url = testdata['address']
        self.login_token = self.get_login_token()

    def get_login_token(self):
        """Получение токена авторизации."""
        try:
            response = requests.post(f'{self.base_url}gateway/login', data={
                'username': testdata['user'],
                'password': testdata['pass']
            })
            response.raise_for_status()
            return response.json()['token']
        except requests.RequestException as e:
            raise Exception(f"Ошибка при получении токена: {e}")

    def create_post(self):
        """Создание поста через API."""
        headers = {'X-Auth-Token': self.login_token}
        post_data = {
            'title': testdata['title'],
            'description': testdata['descript'],
            'content': testdata['cont']
        }
        try:
            response = requests.post(f'{self.base_url}api/posts', json=post_data, headers=headers)
            response.raise_for_status()
            return post_data
        except requests.RequestException as e:
            raise Exception(f"Ошибка при создании поста: {e}")

    def delete_post(self, post_id):
        """Удаление поста через API."""
        headers = {'X-Auth-Token': self.login_token}
        try:
            response = requests.delete(f'{self.base_url}api/posts/{post_id}', headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Ошибка при удалении поста: {e}")
