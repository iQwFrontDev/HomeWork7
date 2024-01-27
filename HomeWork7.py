import requests

#Задание1
class Rate:
    def __init__(self, name='name',format_ = 'value', check = True ):
        self.name = name
        self.format = format_
        self.check = check

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def diff(self, check):
        self.check = check

    def make_format(self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                if self.check == True:
                    difference = response[currency]['Previous'] - response[currency]['Value']
                    return difference
                else:
                    return response[currency]['Value']

            return 'Error'
    def max_cource(self):
        response = self.exchange_rates()
        max_course=0
        for row in response.values():
            value=row['Value']
            if max_course<=value:
                max_course=value

        return row['Name'], max_course

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')


r = Rate()
print(r.max_cource())
print(r.usd())


class Employee:
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority
        self.awards = awards
        self.grade = 1

    def grade_up(self):
        self.grade += 1

    def publish_grade(self):
        print(self.name, self.grade)


class Developer(Employee):
    def __init__(self, name, seniority, awards=0):
        super().__init__(name, seniority, awards=0)

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1

        if self.seniority % 5 == 0:
            self.grade_up()

        return self.publish_grade()


class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority, awards)

    def check_if_it_is_time_for_upgrade(self):
        if self.seniority == 0:
            self.seniority = 1 + self.awards * 2
        else:
            self.seniority += 1
        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()


elena = Designer('Елена', seniority=0, awards=2)
for i in range(20):
    elena.check_if_it_is_time_for_upgrade()



