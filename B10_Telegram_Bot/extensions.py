import re  # just to fill dirty
import json
import requests
from config import currenc


class APIException(Exception):
    pass


class MoneyExchange:
    def __init__(self):
        pass

    def exchange_money(self, first_currency, second_currency, amount):
        first_currency = self.parse_user_input(first_currency)
        second_currency = self.parse_user_input(second_currency)
        self.check_data(first_currency, second_currency, amount)
        return self.get_price(first_currency, second_currency, float(amount))

    #  если пользователь ошибся в воде но несильно
    @staticmethod
    def parse_user_input(currency):
        for i in currenc.values():
            result = re.search(i[1], currency, re.I)
            if result:
                return i[0]
        raise APIException('Укажите пожалуйста действительную валюту из списка /values')

    @staticmethod
    def check_data(first_currency, second_currency, amount):
        if first_currency == second_currency:
            raise APIException('Указана одинаковая валюта')
        try:
            float(amount)
        except ValueError:
            raise APIException(f'не удалось обработать {amount}, укажите число')

    @staticmethod
    def get_price(first_currency, second_currency, amount):
        html = requests.get(f'https://api.exchangeratesapi.io/latest?base={first_currency}').content
        rate = float(json.loads(html)['rates'][second_currency])
        return round(rate*amount, 2)
