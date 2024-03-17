import time
from itertools import count
from data_conversion import (get_vacancies,
                             predict_salary)


def fetch_hh_salaries(language):
    url = 'https://api.hh.ru/vacancies/'
    moscow_city = 1
    publication_period = 30
    vacancies_count_on_page = 100
    vacancies_found = 0
    vacancies_salaries = []
    for page in count(0):
        payload = {
            'text': language,
            'area': moscow_city,
            'period': publication_period,
            'per_page': vacancies_count_on_page,
            'page': page
        }
        page_vacancies = get_vacancies(url, None, payload)
        vacancies_found = page_vacancies['found']
        for vacancy in page_vacancies['items']:
            if not vacancy['salary']:
                continue
            vacancies_salaries.append(predict_rub_salary_hh(vacancy['salary']))
        max_pages_count = 19
        if page >= page_vacancies['pages'] or page >= max_pages_count:
            time.sleep(30)
            break
    return vacancies_salaries, vacancies_found


def predict_rub_salary_hh(vacancy):
    salary_from = vacancy['from']
    salary_to = vacancy['to']
    if vacancy['currency'] == 'RUR':
        return predict_salary(salary_from, salary_to)
    else:
        return None
